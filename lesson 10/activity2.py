def flips(n1,n2):
    f=0
    while (n1>0 or n2>0):
        d1=n1&1
        d2=n2&1
        if(d1!=d2):
            f=f+1
        n1=n1>>1
        n2=n2>>1
    return f  
n1=int(input("Enter first number: ")) 
n2=int(input("Enter second number: "))
print("\n number of flips needed: ",flips(n1,n2))  