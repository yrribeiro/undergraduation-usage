import random

# dist_matrix = [ # 10 cities
#     [0,30,84,56,-1,-1,-1,75,-1,80],
#     [30,0,65,-1,-1,-1,70,-1,-1,40],
#     [84,65,0,74,52,55,-1,60,143,48],
#     [56,-1,74,0,135,-1,-1,20,-1,-1],
#     [-1,-1,52,135,0,70,-1,122,98,80],
#     [70,-1,55,-1,70,0,63,-1,82,35],
#     [-1,70,-1,-1,-1,63,0,-1,120,57],
#     [75,-1,135,20,122,-1,-1,0,-1,-1],
#     [-1,-1,143,-1,98,82,120,-1,0,-1],
#     [80,40,48,-1,80,35,57,-1,-1,0],
# ]

dist = {
    (1, 2): 30,
    (1, 3): 84, (1, 4): 56,
    (1, 8): 75, (1, 10): 80,
    (2, 1): 30,
    (2, 3): 65, (2, 7): 70,
    (2, 10): 40, (3, 1): 84,
    (3, 2): 65,
    (3, 4): 74, (3, 5): 52,
    (3, 6): 55, (3, 8): 60,
    (3, 9): 143, (3, 10): 48,
    (4, 1): 56, (4, 3): 74,
    (4, 5): 135,
    (4, 8): 20, (5, 3): 52,
    (5, 4): 135,
    (5, 6): 70, (5, 8): 122,
    (5, 9): 98, (5, 10): 80,
    (6, 1): 70, (6, 3): 55,
    (6, 5): 70,
    (6, 7): 63, (6, 9): 82,
    (6, 10): 35, (7, 2): 70,
    (7, 6): 63,
    (7, 9): 120, (7, 10): 57,
    (8, 1): 75, (8, 3): 135,
    (8, 4): 20, (8, 5): 122,
    (9, 3): 143,
    (9, 5): 98, (9, 6): 82,
    (9, 7): 120,
    (10, 1): 80, (10, 2): 40,
    (10, 3): 48, (10, 5): 80,
    (10, 6): 35, (10, 7): 57,
}

TOTAL_CITIES = 10
START_CITY = 1
CITIES_TO_VISIT = list(range(1, TOTAL_CITIES+1))

def generate_random_solution(dist_matrix): # generates a random solution, just a combination of cities
    all_edges = list(dist_matrix.keys())
    solution = []
    src = START_CITY
    CITIES_TO_VISIT.remove(src)
    while len(CITIES_TO_VISIT) != 0:
        dst = random.randint(START_CITY, TOTAL_CITIES)
        look = (src, dst)
        if look not in all_edges or dst not in CITIES_TO_VISIT:
            continue
        else:
            solution.append(look)
            CITIES_TO_VISIT.remove(dst)
        src = dst
    solution.append((src, START_CITY))

    return solution

def calculate_route_length(dist_matrix, solution):
    route_length = 0
    for edge in solution:
        route_length += dist_matrix.get(edge)

    return route_length

def get_neighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def get_best_neighbour(dist_matrix, neighbours):
    best_route_length = calculate_route_length(dist_matrix, neighbours[0])
    best_neighbour = neighbours[0]
    for neighbour in neighbours:
        current_route_length = calculate_route_length(dist_matrix, neighbour)
        if current_route_length < best_route_length:
            best_route_length = current_route_length
            best_neighbour = neighbour
    return best_neighbour, best_route_length

def hill_climbing(dist_matrix):
    current_solution = generate_random_solution(dist_matrix)
    # currentSolution = [(1, 4), (4, 3), (3, 8), (8, 5), (5, 6), (6, 9), (9, 7), (7, 2), (2, 10), (10, 1)]
    current_route_length = calculate_route_length(dist_matrix, current_solution)
    neighbours = get_neighbours(current_solution)
    best_neighbour, best_neigh_route_length = get_best_neighbour(dist_matrix, neighbours)

    while best_neigh_route_length < current_route_length:
        current_solution = best_neighbour
        current_route_length = best_neigh_route_length
        neighbours = get_neighbours(current_solution)
        best_neighbour, best_neigh_route_length = get_best_neighbour(dist_matrix, neighbours)

    return current_solution, current_route_length

path, length = hill_climbing(dist)
print(f'ROUTE: {path}\nLENGTH: {length}km')
