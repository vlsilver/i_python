print('','STUDY ABOUT IF - ELSE','',sep = '-------------')
#if-else
#if-elif-elif
Name = 'Nguyen Vang Linhhh'
def convert_list_to_dict_1(lst):
	dct = {}
	for i in lst:
		k = 0
		for j in lst:
			if i == j:
				k += 1
		dct[i] = k
	return dct
kq = convert_list_to_dict_1(list(Name))
print('ket qua 2\t=\t', kq, type(kq))
def convert_list_to_dict_2(lst):
	dct = {}
	for i in lst:
		if i in list(dct.keys()):
			dct[i] +=1
		else:
			dct[i] = 1
	return dct
kq2 = convert_list_to_dict_2(list(Name))
print('ket qua 3\t=\t', kq, type(kq2))

x1 = 1
x2 = -1
x3 = 0
max = x1
if max < x2:
	max = x2
	if max < x3:
		max =x3
elif max < x3:
	max = x3
print('Gia tri lon nhat cua 3 so:\t',max)
