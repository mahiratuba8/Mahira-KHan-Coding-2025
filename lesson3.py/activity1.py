n=int(input('enter the a number to check wether its a palindrome number: '))
num=n
rev=0

while n>0:
    digit=n%10 
    rev=rev*10+digit 
    n=n//10 
    
if(num==rev):
    print(f'{num} is a palindorme number.')
    
else:
    print(f'{num} is not a plindrome number.')
