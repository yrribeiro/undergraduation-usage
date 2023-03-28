import math
import random
import numpy as np

global directions
directions = {'U': lambda x,y: (x-1,y), # up
                'D': lambda x,y: (x+1,y), # down
                'L': lambda x,y: (x,y-1), # left
                'R': lambda x,y: (x,y+1)} # right


def is_pos_available(cand_pos, positions):
    '''
    Check if a candidate position is available within the matrix boundaries and not already taken.
    @params:
    cand_pos - tuple of integers (x, y) representing the candidate position to be checked
    positions - a dictionary containing the positions of all atoms already placed in the matrix

    returns:
    True if the candidate position is available, False otherwise
    '''
    x, y = cand_pos
    if (x < 0 or x > size-1) or (y < 0 or y > size-1) or (x,y) in positions.keys():
        return False
    return True

def str2matrix(s):
    '''
    Map each string atom in order to a matrix position.
    @params:
    s - string with atoms

    returns:
    d - dictionary with (x_pos, y_pos): atom_symbol
    d_instruc - a list with str indicating the steps taken to build the structure
    '''
    global size
    size = len(s)
    is_monster = False
    positions = {}
    dir_instructions, dir_cache = [],[]
    for idx, char in enumerate(s):
        if idx == 0:
            x_pos, y_pos = (random.randint(0,size-1),random.randint(0,size-1))
            positions[(x_pos, y_pos)] = char
            first_atom_position = list(positions.items())[0]
        else:
            candidate_dir = random.choice(list(directions.keys()))

            while not is_pos_available(directions[candidate_dir](x_pos, y_pos), positions) and len(dir_cache) < 4:
                if candidate_dir not in dir_cache: dir_cache.append(candidate_dir)
                candidate_dir = random.choice(list(directions.keys()))

            x_pos, y_pos = directions[candidate_dir](x_pos, y_pos)
            positions[(x_pos, y_pos)] = char
            dir_instructions.append(candidate_dir)
            dir_cache.clear()

    return positions, (first_atom_position, dir_instructions), is_monster

def get_all_atoms_position(s, child_info):
    '''
    Takes the list of directions and uses it to generate the (x, y) coordinates for each atom in the structure
    '''
    positions = {}
    first, dir_instructions = child_info

    for idx, d in enumerate(dir_instructions):
        if idx == 0:
            x_pos, y_pos = first[0][0], first[0][1]
            positions.update([first])
        else:
            x_pos, y_pos = directions[d](x_pos, y_pos)
            positions[(x_pos, y_pos)] = s[idx]
    return positions

def evaluate(positions):
    '''
    Calculates the proposed structure total energy (number of H atoms in adjacency to each H atom) using
    immediate surrounding distance, except diagonals
    @params:
    positions - a dictionary containing the proposed positions of each atoms in 2D space

    returns:
    tot_energy - a integer representing the total number of Hs in the neighborhood. The amount of H in
    whole structure would be tot_energy + 1 then
    '''
    h_count = [pos[0] for pos in positions.items() if pos[1] == 'H']
    tot_energy = 0
    for prev_h_idx in range(len(h_count)-1):
        for post_h_idx in range(prev_h_idx+1, len(h_count)):
            if np.sum(np.abs(np.subtract(h_count[prev_h_idx], h_count[post_h_idx]))) == 1:
                tot_energy += 1

    return tot_energy*2

def is_monster(positions):
    if len(positions) < size:
        return True
    for pos in positions.keys():
        x,y = pos
        if (x < 0 or x > size-1) or (y < 0 or y > size-1):
            return True

    return False

def mutate(positions):
    '''
    Randomly change the direction of a random atom in the structure
    '''
    dir_cache = []
    pos_list = list(positions.items())
    random_pos = random.choice(pos_list)
    new_dir = random.choice(list(directions.keys()))
    while not is_pos_available(directions[new_dir](*random_pos[0]), positions) and len(dir_cache) < 4:
        if new_dir not in dir_cache: dir_cache.append(new_dir)
        new_dir = random.choice(list(directions.keys()))
    positions.pop(random_pos[0])
    positions[directions[new_dir](*random_pos[0])] = random_pos[1]
    dir_cache.clear()

    return positions

def build_2d_matrix(best_structure, best_fitness):
    matrix = np.empty((size, size), dtype=object)
    matrix.fill(' ')
    positions = best_structure[0]
    for pos in positions.items():
        x,y = pos[0]
        matrix[x][y] = pos[1]
    print(f'Molecule structure:\n{matrix}\n- Path from first atom:\n{best_structure[1][1]}\nFREE ENERGY SCORE: {best_fitness}')


def begin_search(s, pop_size=250, max_generations=200, tournament_size=3, global_mutation_rate=0.05):
    population = [str2matrix(s) for _ in range(pop_size)]
    nof_h_atoms = s.count('H')
    best_fitness = -1

    for generation in range(max_generations):
        if best_fitness >= 2*nof_h_atoms or generation == max_generations - 1:
            break

        fitnesses = [evaluate(idv) if not monster_flag else -100 for idv, _, monster_flag in population]
        best_idx, best_fitness = max(enumerate(fitnesses), key=lambda x:x[1])
        best_structure = population[best_idx]

        new_population = ()
        while len(new_population) < pop_size:
            tournament = random.sample(population, tournament_size)
            parent1 = max(tournament, key=lambda x: evaluate(x[0]))[1]
            tournament = random.sample(population, tournament_size)
            parent2 = max(tournament, key=lambda x: evaluate(x[0]))[1]

            crossover_point = random.randint(1, len(s))
            child1, child2 = [], []
            child1.append(parent1[0]) # the info about the first atom position
            child1.append(parent1[1][:crossover_point] + parent2[1][crossover_point:])
            if random.random() < global_mutation_rate:
                child1_positions = mutate(get_all_atoms_position(s, child1))
            else:
                child1_positions = get_all_atoms_position(s, child1)
            child1 = (child1_positions, child1, is_monster(child1_positions))

            child2.append(parent2[0])
            child2.append(parent2[1][:crossover_point] + parent1[1][crossover_point:])
            if random.random() < global_mutation_rate:
                child2_positions = mutate(get_all_atoms_position(s, child2))
            else:
                child2_positions = get_all_atoms_position(s, child2)
            child2 = (child2_positions, child2, is_monster(child2_positions))

            new_population += (child1, child2)

        population = new_population

    return build_2d_matrix(best_structure, best_fitness)



if __name__ == '__main__':
    mol_str = 'HHPPPHHH'
    print(f'\nMolecule chain: {mol_str}\n{begin_search(mol_str)}')