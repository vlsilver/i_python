A = [1000,1,2,3,5,2,5,1,6,7,2,3]
A.sort()
print('ket qua 1\t=\t:',A)
A_1 = [1000,1,2,3,5,2,5,1,6,7,2,3]
B=sorted(A_1)
#print(A_1)
print('ket qua 2\t=\t:',B)
#def sort_list(srt):
def sort_list(srt):
	kq = []
	for i in range(0,len(srt)):
		kq.append(min(srt))
		srt.remove(min(srt))
	return kq 
print('ket qua 3\t=\t:',sort_list(A_1))
A = [1000,1,2,3,5,2,5,1,6,7,2,3]


def min_(lst):
	mn = lst[0]
	for i in range(0,len(lst)):
		if lst[i] <= mn:
			mn = lst[i]
	return mn
def sort(lst):
	kq = []
	for i in range(0,len(lst)):
		kq.append(min_(lst))
		lst.remove(min_(lst))
	return kq
print('ket qua 4\t=\t:',sort(A))
 	