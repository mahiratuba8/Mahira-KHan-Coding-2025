def power(x,y):
    temp=1
    while(y>0):
        if (y%2==0):
            x=x*x
            y=y>>1
        else:
            temp=temp*x
            y=y-1
    return temp
x=int(input("Enter base: "))
y=int(input("Enter exponent: "))

print(power(x,y))