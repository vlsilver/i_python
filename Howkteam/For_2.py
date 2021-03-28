def bt3(n):
	A =[[0]*n for i in range(n)]
	x = 0
	y = -1
	j = 0
	for i in range(n*n):
		if x == j and y < n-1-j:
			x += 0
			y += 1
		elif y == n-1 -j and x < n-1-j:
			x += 1
			y += 0
		elif x == n-1-j and y > j:
			x += 0
			y -= 1
		elif y == j and x > j+1:
			x -= 1
			y += 0
		else:
			j+=1
			y+=1
		A[x][y] = i
	for dx in range(n):
		for dy in range(n):
			print("%02i" % A[dx][dy], end = ' ')
		print()
	return A
print(bt3(10))
