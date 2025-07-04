b = int(input('Enter your binary number: '))

def binaryToDecimal(n):
    d, p = 0, 0
    while n:
        d += (n % 10) * (2 ** p)
        n //= 10
        p += 1
    print("Decimal:", d)

binaryToDecimal(b)