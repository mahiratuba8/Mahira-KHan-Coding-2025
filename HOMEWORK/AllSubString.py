import math
def power_set(letters, setsize):
    powersetsize = int(math.pow(2, setsize))
    outer=0
    inner=0
    for outer in range(powersetsize):
        for inner in range(setsize):
            if (outer & (1 << inner)) > 0:
                print(letters[inner], end="")
        print("")


word = input("Enter string: ")
set = list(word)      
setsize = len(set)     
power_set(set, setsize) 
