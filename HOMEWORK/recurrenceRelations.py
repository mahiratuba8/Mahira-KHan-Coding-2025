def myfunction1(n):
    if(n>0):
        return
    for i in range (o,n+1):
        print('codingal')
    myfunction1(n/2)
    myfunction1(n/3)
def myfunction2():
    if(n<=1):
        return
    print('Codingal')
    myfunction2(n-1)

    #tree method results to t(n/2*2)+ t(n/2*3)+t(n/3*2)+t(n/3*3)
    #according to t(n)=t(n**k)+O(n)
    #n=n**k
    #logn=k(nlogn)=k(logn)=O(nlogn)
    #time complexity=O(nlogn)
    #     