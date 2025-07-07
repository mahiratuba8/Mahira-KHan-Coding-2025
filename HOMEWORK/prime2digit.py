def prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n&1==0:
        return False
    for i in range (3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
start=int(input('enter the start range: '))
end=int(input('enter the end range: '))
for n in range(start,end+1):
    if n>=10 and n<=99:
        if prime(n):
            print(n,end=" ")