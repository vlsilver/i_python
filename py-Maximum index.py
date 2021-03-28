#code
T = int(input())
for t in range(T):
    A = [int(x) for x in input().split()]
    num_ = len(A)
    Done_ = False
    for i in range(num_):
        for j in range(0,i+1):
            idex_max = num_ - i + j -1
            if A[idex_max] >= A[j]:
                Done_ = True
                break
        if Done_:
            break
    print(idex_max - j)