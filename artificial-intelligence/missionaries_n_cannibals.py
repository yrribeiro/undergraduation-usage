INITIAL_STATE = [3, 3, 0, 0, 0]
# State representation:
# [
#   number of MISSIONARIES on LEFT side of the river,
#   number of CANNIBALS on LEFT side of the river,
#   number of MISSIONARIES on RIGHT side of the river.
#   number of CANNIBALS on RIGHT side of the river,
#   boat direction (0 for left margin, 1 for right margin)
# ]

VALID_MOVES = [(1, 0), (1, 1), (2, 0), (0, 2)] # (M, C) --> move M missionaries and C cannnibals
path, visited_states = [], []

def traverse_river(current_state, nof_miss=0, nof_cann=0):
    if nof_miss + nof_cann > 2: return

    if not current_state[-1]:                # boat is on the left side
        src_miss_idx, src_cann_idx = 0, 1
        dst_miss_idx, dst_cann_idx = 2, 3
    else:                                # boat is on the right side
        src_miss_idx, src_cann_idx = 2, 3
        dst_miss_idx, dst_cann_idx = 0, 1

    if current_state[src_miss_idx] == 0 and current_state[src_cann_idx] == 0: return # there's no one to traverse the river

    current_state[-1] = 1 - current_state[-1] # updating the boat direction

    for traversal in range(min(nof_miss, current_state[src_miss_idx])):
        current_state[src_miss_idx] -= 1
        current_state[dst_miss_idx] += 1
    for traversal in range(min(nof_cann, current_state[src_cann_idx])):
        current_state[src_cann_idx] -= 1
        current_state[dst_cann_idx] += 1

    return current_state

def generate_successors(current_state):
    successors = []
    for (m, c) in VALID_MOVES:
        state_after_traversal = traverse_river(current_state[:], m, c)
        if is_valid_state(state_after_traversal):
            successors.append(state_after_traversal)

    return successors

def is_valid_state(state):
    flag = True
    if (state == None) or (state in visited_states):
        flag = False
    if (state[0] < state[1] and state[0] > 0) or (state[2] < state[3] and state[2] > 0):
        flag = False
    return flag

def get_next_unvisited_state(state_to_check):
    suc = generate_successors(state_to_check)
    return suc[0] if len(suc) > 0 else -1

def is_final_state(state):
    return True if (state[2] == 3) and (state[3] == 3) else False

def dfs(INITIAL_STATE):
    path.append(INITIAL_STATE)
    while len(path) != 0:
        state_to_check = path[len(path)-1]
        if is_final_state(state_to_check):
            break
        next_state = get_next_unvisited_state(state_to_check)
        if next_state == -1:
            path.pop()
        else:
            visited_states.append(next_state)
            path.append(next_state)

    return path

solution = dfs(INITIAL_STATE)

for i in range(1, len(solution)):
    delta_miss = abs(solution[i][0] - solution[i-1][0])
    delta_cann = abs(solution[i][1] - solution[i-1][1])
    delta_boat = solution[i][4] - solution[i-1][4]

    if delta_boat == 1:
        direction = '->'
    else:
        direction = '<-'

    print(f'STATE: {solution[i-1]}\n    do: {(delta_miss, delta_cann, direction)}\n')