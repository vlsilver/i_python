def matrix(A):
	n = len(A)
	n = n-1
	print("Matrix brfore rotate 90")
	for dx in range(len(A)):
		for dy in range(len(A)):
			print("%02d" % A[dx][dy], end = " ")
		print()
	for i in range(n):
		for j in range(i,n-i):
			k1 = A[j][n-i]
			A[j][n-i] = A[i][j]
			k2 = A[n-i][n-j] 
			A[n-i][n-j] = k1
			k3 = A[n-j][i]
			A[n-j][i] = k2
			A[i][j] = k3
	print("Matrix after rotate 90")
	for dx in range(len(A)):
		for dy in range(len(A)):
			print("%02d" % A[dx][dy], end = " ")
		print()
matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])