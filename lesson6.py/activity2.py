def setornot(num,bit):
    if num&(1<<(bit-1)):
        print('\n set')
    else:
        print('\n not set')
num=int(input('enter a number: '))
position=int(input('neter the postion of the bit: '))
setornot(num,position)