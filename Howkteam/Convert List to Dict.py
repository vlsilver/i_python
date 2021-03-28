A = [13,2,2,1,2,1,2,13,2,2,2,2,2]
def convert_list_to_dict(lst):
	st = set(lst)
	dct = {}
	for i in st:
		dct[i] = lst.count(i)
	return dct
kq = convert_list_to_dict(A)
print('ket qua 1\t=\t', kq, type(kq))
#print('Ket qua can chuyen',A_TO_DIC,type(A_TO_DIC))

def convert_list_to_dict_1(lst):
	dct = {}
	for i in lst:
		k = 0
		for j in lst:
			if i == j:
				k += 1
		dct[i] = k
	return dct
kq = convert_list_to_dict_1(A)
print('ket qua 2\t=\t', kq, type(kq))
#print('Ket qua can chuyen',A_TO_DIC,type(A_TO_DIC))

def convert_list_to_dict_2(lst):
	dct = {}
	for i in lst:
		if i in list(dct.keys()):
			dct[i] +=1
		else:
			dct[i] = 1
	return dct
kq2 = convert_list_to_dict_2(A)
print('ket qua 3\t=\t', kq, type(kq))

from collections import Counter
print('ket qua 4\t=\t', dict(Counter(A)), type(dict(Counter(A)))) 

#print('Ket qua can chuyen',A_TO_DIC,type(A_TO_DIC))
B = [100,1000,4,5,1,2,5,6,41,7]
print(set(B))