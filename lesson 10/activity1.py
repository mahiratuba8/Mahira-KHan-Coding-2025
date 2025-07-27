import math
def power_set(set,setsize):
    powersetsize=(int)(math.pow(2,setsize))
    outer=0
    inner=0
    for outer in range (0,powersetsize):
        for inner in range (0,setsize):
            if((outer&(1<<inner))>0):
                print(set[inner],end="")
        print("")
size=int(input("Enter array size: "))
set=[]
for i in range(0,size):
    n=int(input("Enter element"))
    set.append(n)
power_set(set,len(set))
    