def swap1(a,b):
    a=a^b
    b=a^b
    a=a^b
    print("after swapping: ",a,b)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

swap1(a,b)