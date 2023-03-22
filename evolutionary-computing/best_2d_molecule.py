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
    '''
    size = len(mol_str)
    positions = {}
    x_pos, y_pos = (random.randint(0,size-1),random.randint(0,size-1))
    positions[(x_pos, y_pos)] = s[0]

    for i in range(1,size):
        if i%2 == 0: # insert in row
            y_pos = random.randint(0,size-1)
            while ((x_pos, y_pos) in positions.keys()):
                y_pos = random.randint(0,size-1)
        else: # insert in column
            x_pos = random.randint(0,size-1)
            while ((x_pos, y_pos) in positions.keys()):
                x_pos = random.randint(0,size-1)
        positions[(x_pos, y_pos)] = s[i]

    return positions

def evaluate(positions):
    '''
    Calculates the proposed structure total energy (maximum number of H atoms in adjacency) using
    euclidean distance between points
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

    return tot_energy

def begin_search(s, pop_size=100, max_generations=1000):
    population = [str2matrix(s) for _ in range(pop_size)]
    nof_h_atoms = s.count('H')
    best_fitness = -math.inf
    best_structure = None

    for generation in range(max_generations):
        if best_fitness >= nof_h_atoms-1 or generation == max_generations - 1:
            break

        fitnesses = [evaluate(idv) for idv in population]
        best_idx, best_fitness = max(enumerate(fitnesses), key=lambda x:x[1])
        best_structure = population[best_idx]

        new_population = []
        while len(new_population) < pop_size:
            parent1 = 
            parent2 = 



if __name__ == '__main__':
    mol_str = 'HHPPH'
    print(begin_search(mol_str))