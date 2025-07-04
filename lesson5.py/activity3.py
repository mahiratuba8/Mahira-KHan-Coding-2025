def numberofbits(n):
    count=0
    while(n):
        count=count+1
        n=n>>1
    return count
n=int(input('enter a number: '))
print('total bits: ', numberofbits(n))
