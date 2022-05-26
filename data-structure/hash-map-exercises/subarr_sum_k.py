# leetcode question 560 - Number of contiguous subarray whose sum is equal to K
def calculate_sum(arr, k):
    tot = 0
    curr_sum = 0
    prefix_sums = {0:1}
    for n in arr:
        curr_sum += n
        diff = curr_sum - k
        tot += prefix_sums.get(diff, 0)
        prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
        # print('n = ', n, curr_sum, diff, tot, prefix_sums[curr_sum])

    return tot


print(calculate_sum([2,3,5,1,6,4,2,1], 6))
