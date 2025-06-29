def myfunction(n):
    for i in range (0,n+1):
        print('First Loop') #O(n)
    j=1
    while(j<=n+1):
        print("second loop", j) #O(logn)
        j=j*2
    for i in range(0,100):
        print('third loop') #O(1)

# o(n)+o(logn)+o(1)= O(n)