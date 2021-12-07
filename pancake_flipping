def flip(A, k):
    start = 0
    while start < k:
        A[start], A[k] = A[k], A[start]
        k -= 1
        start += 1

def pancake_flipping(A):
    n = len(A)
    all_flips = []
    while n > 1:
        max_index = A.index(max(A[:n]))
        flip(A, max_index)
        flip(A, n-1)
        all_flips.append(max_index)
        all_flips.append(n-1)
        n -= 1
    return all_flips

A = [5, 1, 4, 2, 3]
print(f'Original array  = {A}')
flip = pancake_flipping(A)
print(f'Flip sequence = {flip}\nTotal flips = {len(flip)}')
print(f'Final array = {A}')
