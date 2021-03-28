def find_index_with_given_sum(A,S):
	SUM_S = 0
	i = 0
	j = 0
	while i < len(A):
		SUM_S += A[i]
		while SUM_S > S and (j<i):
			SUM_S -= A[j]
			j += 1
		if SUM_S == S:
			print(SUM_S,[j,i])
			break
		if i == len(A) -1:
			print(-1)
		i+=1
find_index_with_given_sum([1,2,3,7,5],12)