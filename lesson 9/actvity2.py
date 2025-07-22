def swap1(a,b):
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print("After swapping: ", a, b)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

swap1(a,b)