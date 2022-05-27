def numberOfWays(arr, k):
    num_ocurr = {}
    tot = 0
    for i in arr:
      if i in num_ocurr:
        num_ocurr[i] += 1
      else:
        num_ocurr[i] = 1
        
    for i in arr:
      diff = k-i
      tot += num_ocurr.get(diff, 0)
      
    return int(tot/2)

print(numberOfWays([1, 2, 3, 4, 3], 6))