def p_4(n):
    count=0
    if(n&(~(n&(n-1)))):
        while(n>1):
            n=n>>1
            count=count+1
        if(count%2==0):
            return True
        else:
            return False
n=int(input("Enter a number: "))
if(p_4(n)):
    print("The number is a power of 4")
else:
    print("The number is not a power of 4")