def MultiplyLoops(n,m):
  return n*m

def MultiplyN(n,m):
  result= 0
  for i in range(n):
    result += m
  return result

print(MultiplyLoops(2,3))
print(MultiplyLoops(8,9))

print(MultiplyN(5,6))
print(MultiplyN(4,7))
  