def spiral_matrix(n):
    start = 0
    s_old = []
    for i in range(n):
        print(s_old)
        s = []
        for j in range(n):
            print(s,i,j)
            if i == j:
                if not s:
                    s.append(start)
                else:
                    if i + j >= n:
                        s.append(s[-1] - 1)
                    else:
                        s.append(s[-1] + 1)
            elif i > j:
                if i + j >= n:
                    s.append(s[-1] - 1)
                else: # i + j < n
                    if j == i - 1:
                        start += 4*(n - 2*i + 1)  
                        s.append(start - 1)
                    else:
                        s.append(s_old[j] - 1)
            else: # i < j
                if i + j >= n:
                    s.append(s_old[j] + 1)
                else:
                    s.append(s[-1] + 1)
            print(s,i,j)
        s_old = s.copy()
        print(" ".join("{:02d}".format(e) for e in s_old))
print(spiral_matrix(5))