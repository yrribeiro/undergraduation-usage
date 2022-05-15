import time

def power(M, n):
  mAux = [
    [1, 1],
    [1, 0]
  ]
  for i in range(2, n+1):
    upperLeft = M[0][0]*mAux[0][0] + M[0][1]*mAux[1][0]
    upperRight = M[0][0]*mAux[0][1] + M[0][1]*mAux[1][1]
    bottomLeft = M[1][0]*mAux[0][0] + M[1][1]*mAux[1][0]
    bottomRight = M[1][0]*mAux[0][1] + M[1][1]*mAux[1][1]

    M[0][0] = upperLeft
    M[0][1] = upperRight
    M[1][0] = bottomLeft
    M[1][1] = bottomRight

def matrixFibonacci(n):
  M = [
    [1, 1],
    [1, 0]
  ]
  if n==0:
    return 0
  power(M, n-1)
  return M[0][0]

n = 970500
start = time.time()
print(matrixFibonacci(n))
end = time.time()
print(f'\nexecution time: {end-start}')
