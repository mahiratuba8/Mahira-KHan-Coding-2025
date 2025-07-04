def isevenorodd(n):
    if(n^1==n+1):
        return True
    else:
        return False
n=int(input('Enter a number: '))
if isevenorodd(n):
    print(f'{n} is even')
else:
    print(f'{n} is odd')