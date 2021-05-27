from sys import maxsize as MAXSIZE
from itertools import permutations
vertex = 4

def calculate_min_route(graph, ini):
    all_vertex = []
    for i in range(vertex):
        if i != ini:
            all_vertex.append(i)
 
    min_path = MAXSIZE
    v_permutation = permutations(all_vertex)
    min_route = []
    ant_sum = MAXSIZE
    for i in v_permutation:
        current_path_weight = 0
        src = ini
        for j in i:
            current_path_weight += graph[src][j]
            src = j
        current_path_weight += graph[src][ini]
        if current_path_weight<ant_sum:
            ant_sum = current_path_weight
            min_route.insert(0, i)
        min_path = min(min_path, current_path_weight)

    return min_path, min_route[0]

if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20], 
        [10, 0, 35, 25],
        [15, 35, 0, 30], 
        [20, 25, 30, 0]
    ]
    ini = 2 # initial vertex/city
    result = list(calculate_min_route(graph, ini))
    print('CIDADE INICIAL: {}\nOrdem de visita: {}\nDistância à percorrer: {}km'.format(ini, result[1], result[0]))
