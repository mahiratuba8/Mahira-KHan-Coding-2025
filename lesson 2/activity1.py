number=int(input('Enter a number: '))
power= len(str(number))
result=0
temp=number
while temp>0:
    digit=temp%10
    result=result+digit**power
    temp=temp//10
if number==result:
    print(f'{number} is an Amstrong number.')
else:
    print('this is not an Amstrong number.')