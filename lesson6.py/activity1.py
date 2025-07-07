def number_bits(n):
    one=0
    zeros=0
    while(n):
        if(n&1==1):
            one=one+1
        else:
            zeros=zeros+1
        n=n>>1
    print('\n one=',one,'\n zeros=',zeros)
num=int(input('enter a number: '))

number_bits(num)