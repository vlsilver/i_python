def find_largest_area(A):
	max_ = 0
	i_ = 0
	j_ = 0
	A_i = 0
	A_j = 0
	for i in range(0,len(A)):
		for j in range(i+1,len(A)):
			if A[j] > A[i]:
				max_j = abs((j-i)*A[i])
			else:
				max_j = abs((j-i)*A[j])
			if max_j > max_:
				max_ = max_j
				i_ = i + 1
				j_ = j + 1
				A_i = A[i]
				A_j = A[j]
	return max_,[i_,A_i],[j_,A_j]


if __name__ == "__main__":
    print(find_largest_area([4,5,5,6]))