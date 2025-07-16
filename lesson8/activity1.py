def p_2(n):
    if(n==0):
        return 0
    if((n&(~(n-1)))==n):
        return 1
    return 0
n=int(input("Enter a number: "))
if(p_2(n)):
    print("The number is power of 2")
else:
    print("The number is not a power of 2")