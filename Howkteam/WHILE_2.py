x = 0
A = []
while len(A) < 5:
	x +=1
	if x % 2 == 0:
		A.append(x)
print(A)
A.clear()
x=0
while True:
	x+=1
	if x % 2 == 0 & len(A) < 4:
		A.append(x)
		continue
	elif len(A) > 4:
		break
print(A)
with open('vlsilver.txt',mode = 'r+') as f:
	while True:
		i = 0
		st = ''
		row = f.readline()
		if len(row) == 0:
			break
		A = row.split(' ',row.count(' '))
		while i < len(A) -1:
			i+=1
			if A[i] == 'Kteam':
				A[i-1] = 'How'
			#st = st+A[i-1]+' '
			#if i == len(A)-1:
				#st = st + A[i]
		with open('Kteam.txt', mode = 'a+') as kt:
			kt.write(str(A))
	f.seek(0)
	a = f.read()
	B = a.split(' ',a.count(' '))
	i = 0
	print(a)
	print(B)
	while i < len(B)-1:
		i+=1
		if B[i] == 'Kteam' or B[i] == 'kteam':
			B[i-1] = 'How'
		with open('Kteam3.txt', mode = 'a+') as kt1:
			kt1.write(B[i-1]+' ')
			if i == len(B) -1:
				kt1.write(B[i])
DS = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]