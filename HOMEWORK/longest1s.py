def longest_1(n):
    count=0
    while n:
        n=n&(n<<1)
        count=count+1
    return count 
n=int(input("Enter a number: "))
print(longest_1(n))