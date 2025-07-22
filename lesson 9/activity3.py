def divide(divident,divisor):
    sign=(-1 if((divident<0)^(divisor<0)) else 1)
    divisor=abs(divisor)
    divident=abs(divident)
    q=0
    temp=0
    for i in range (31,-1,-1):
        if(temp+(divisor<<i)<=divident):
            temp=temp+divisor<<i
            q=q|1<<i
    if sign==-1:
        q=-q
    return q
divident=int(input("Enter divident: "))
divisor= int(input("Enter  divisor: "))

print("Result: ",divide(divident,divisor))