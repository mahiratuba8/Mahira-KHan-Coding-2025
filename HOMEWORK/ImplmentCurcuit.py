#def solve_circuit(a,b,c):
    #return ~(a&b)|~c
#print("A B C | Q")
#for i in range (8):
    #a=(i>>2)&1
    #b=(i>>1)&1
    #c=i&1
    #q=solve_circuit(a,b,c)&1
    #print(f"{a},{b},{c}|{q}")

#Simple one line solution
A,B,C=map(int,input("Enter A B and C: ").split())
print(f"output Q: {(~(A&B)|~C)&1}")