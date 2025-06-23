a = int(input('Enter a for a*b : '))
b = int(input('Enter b for a*b : '))
def MultiplyLoops(n,m):
  return n*m

def MultiplyN(n,m):
  result= 0
  for i in range(n):
    result += m
  return result

print('1 iteration answer: ', MultiplyLoops(a,b))

print('N iteration answer: ', MultiplyN(a,b))