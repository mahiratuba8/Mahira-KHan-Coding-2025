import math
def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)


num= int(input('enter a number:'))
num2 = int(input('enter a number:'))
print('lcm: ', lcm(num,num2))
