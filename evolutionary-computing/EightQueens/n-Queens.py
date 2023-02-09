import random
import itertools
from scipy import special as sc

NUM_QUEENS = 4
SIZE_POPULATION = NUM_QUEENS+2
MUTATION_RATE = 0.05

def generate_population():
    return [random.sample(range(0,NUM_QUEENS), NUM_QUEENS) for i in range(SIZE_POPULATION)]

def evaluate_idv(idv):
    score = 0

    for row_i in range(NUM_QUEENS):
        col = idv[row_i]
        for row_j in range(NUM_QUEENS):
            if row_j == row_i:
                continue
            if idv[row_j] == col:
                continue
            if row_j + idv[row_j] == row_i + col:
                continue
            if row_j - idv[row_j] == row_i - col:
                continue
            score += 1

    return score/2

def is_best_gen(population):
    for idv in population:
        score = evaluate_idv(idv)
        if score == sc.comb(NUM_QUEENS, 2):
            print('SOLUTION FOUND')
            print(f'{idv}. Score: {score}')
            return True
    return False

def select_by_score(population):
    return [idv for idv in population if random.randrange(sc.comb(NUM_QUEENS, 2)*2) < evaluate_idv(idv)]

def crossmutate(parents):
    cross_points = random.sample(range(NUM_QUEENS), 1)
    offsprings = []
    permutations = list(itertools.permutations(parents, 2))

    for perm in permutations:
        offspring = []
        start_pt = 0

        for parent_idx, cross_point in enumerate(cross_points):
            parent_part = perm[parent_idx][start_pt:cross_point]
            offspring.append(parent_part)
            start_pt = cross_point

        last_parent = perm[-1]
        parent_part = last_parent[cross_point:]
        offspring.append(parent_part)
        offsprings.append(list(itertools.chain(*offspring)))

    for row in range(len(offsprings)):
        if random.random() < MUTATION_RATE:
            offsprings[row] = random.randrange(NUM_QUEENS)

    return offsprings

def generate_next_gen(prev_pop):
    parents = select_by_score(prev_pop)
    next_pop = crossmutate(parents)
    for idv in prev_pop:
        next_pop.append(idv)

    return sorted(next_pop, key=lambda idv: evaluate_idv(idv), reverse=True)[:SIZE_POPULATION]

population = generate_population()
gen = 0

while not is_best_gen(population):
    print(f'~ GENERATION: {gen}')
    population = generate_next_gen(population)
    gen += 1