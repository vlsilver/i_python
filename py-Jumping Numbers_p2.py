N = int(input())
n = len(str(N))
for i in range(1,n+1):
    A = [0]*i
    m =1
    while m < 10:
        a = m
        for j in range(0,i):
            A[j] = a
            a = a -1
            print(A[j],end='')
        print(end=' ')
        a = m
        for j in range(0,i):
            A[j] = a
            a = a + 1
            print(A[j],end='')
        print(end=' ')
        m += 1

