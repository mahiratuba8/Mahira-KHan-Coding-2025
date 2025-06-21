def onsquaretime(n):
    iteration=0
    for i in range(0,n):
        for j in range(0,n):
            print('*',end=' ')
            iteration=iteration+1
        print('')
    print('\n')
onsquaretime(3)
onsquaretime(4)
onsquaretime(5)
