def n_in_A(lst,value):
	for i in range(len(lst)):
		if value == lst[i]:
			n_in_A = True
			break
		else:
			n_in_A = False
	return n_in_A
def bt(A,k):
	for i in range(len(A)):
		n = k - A[i]
		m = n_in_A(A,n)
		if m == True and n != A[i]:
			break		
		if n == A[i]:
			m = False
	return m
print(bt([1,2,3,4,5,6],12))
def tich(A):
	A_tich = [0 for i in range(len(A))]
	for i in range(len(A)):
		tich = 1
		for j in range(len(A)):
			if j != i:
				tich = tich*A[j]
		A_tich[i] = tich
	return A_tich
print(tich([1,2,3,4,5]))

def get_top(lst):
	k = 3
	top_min = lst[0:k]
	for i in range(k,len(lst)):
   		if lst[i] <= top_min[0]:
   			if top_min[1] <= top_min[2]:
   				top_min[2] = top_min[1]
   			if top_min[0] <= top_min[1]:
   				top_min[1] = top_min[0]
   			top_min[0] = lst[i]
 	  	else:
   			if lst[i] <= top_min[1]:
   				if top_min[1] <= top_min[2]:
   					top_min[2] = top_min[1]
   				top_min[1] = lst[i]
   			else:
   				if lst[i] <= top_min[2]:
   					top_min[2] = lst[i]
	return top_min

print(get_top([432,431,710,366,837,956]))