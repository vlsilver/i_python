# dùng break thì sẽ không chạy else
# dùng continue thì vẫn chạy else
#for - break - continue - else
#OUTPUT for VARIABLE in DATA dieu kien
#enumberate(List,start) tao ra gia tri va so thu tu



def sum(set_):
	#set_ = list(set_)
	sum = 0
	for i in set_:
		sum = sum + i
	return sum
print(sum({5,8,1,9,4}))

def bt1(lst1):
	for i in lst1:
		i[0] = None
	return lst1
print(bt1([[1,2,3],[4,5,6]]))

def bt2(n):
	A_nxn = []
	for i in range(1,n*n+1):
		for j in range(1,n+1):
			if i == j*n:
				A_i = ([k for k in range(i-n,i)])
				A_nxn.append(A_i)
	return A_nxn
	for x in range(n):
		for y in range(n):
			print(A[x][y], end = ' ')
print(bt2(5))

A =[1,2,3,4,5]
print(list(enumerate(A)))
