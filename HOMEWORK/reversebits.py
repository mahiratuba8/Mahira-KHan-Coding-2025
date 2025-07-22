def reverse_bits(n):
    result=0
    while n:
        result=(result<<1)|(n&1)
        n=n>>1
    return result 
n=int(input("enter a number: "))
print(f"orignal number {n}, binary number {bin(n)}")
print(f"reversed number {reverse_bits(n)}, binary number {bin(reverse_bits(n))}")