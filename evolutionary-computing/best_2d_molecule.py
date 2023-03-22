import math
import random
import numpy as np

def str2matrix(s):
    '''
    Map each string atom in order to a matrix position.
    @params:
    s - string with atoms

    returns:
    d - dictionary with (x_pos, y_pos): atom_symbol
    d_instruc - a list with str indicating the steps taken to build the structure
    '''
    size = len(mol_str)
    positions = {}
    x_pos, y_pos = (random.randint(0,size-1),random.randint(0,size-1))
    positions[(x_pos, y_pos)] = s[0]
    directions = {'U': lambda x,y: (x-1,y),
                  'D': lambda x,y: (x+1,y),
                  'L': lambda x,y: (x,y-1),
                  'R': lambda x,y: (x,y+1)}
    dir_instructions = [random.choice(list(directions.keys())) for _ in range(size-1)]

    for idx, d in enumerate(dir_instructions, start=1):
        x_pos, y_pos = directions[d](x_pos, y_pos)

        while (x_pos < 0 or x_pos > size-1) or (y_pos < 0 and y_pos > size-1):
            x_pos, y_pos = directions[d](x_pos, y_pos)

        positions[(x_pos, y_pos)] = s[idx]

    return positions, dir_instructions

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

def begin_search(s, pop_size=100, max_generations=1000):
    population = [str2matrix(s) for _ in range(pop_size)]
    nof_h_atoms = s.count('H')
    best_fitness = -math.inf
    best_structure = None

    for generation in range(max_generations):
        if best_fitness >= 2*nof_h_atoms or generation == max_generations - 1:
            break

        fitnesses = [evaluate(idv) for idv, _ in population]
        best_idx, best_fitness = max(enumerate(fitnesses), key=lambda x:x[1])
        best_structure = population[best_idx]

        # new_population = []
        # while len(new_population) < pop_size:
        #     parent1 = 
        #     parent2 = 



if __name__ == '__main__':
    mol_str = 'HHPPH'
    # print(begin_search(mol_str))
    print(str2matrix(mol_str))