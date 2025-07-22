def power_8(n):
    return n>0 and (n&(n-1))==0 and n%7==1
n=int(input("Enter a number: "))
if power_8(n):
    print("Power of 8")
else:
    print("Not power of 8")

