def first_bit_pos(n):
    if n == 0:
        return 0  

    position = 1
    while (n & 1) == 0:
        n = n >> 1
        position += 1

    return position


num = int(input("Enter number: "))
pos = first_bit_pos(num)
print("Position of the first set bit:", pos)