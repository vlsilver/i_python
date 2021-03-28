#while - break
#while - continue
#while - else
print('','STUDY ABOUTE WHILE','',sep = '-----------------------')
print('','MAKE A CODE GET OUTE FIVE VARIABLE %2 == 0','',sep = '...................')
DS = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
DScopy = DS.copy()
print(DScopy)
i = 0
f = 11
while i < len(DScopy):
	if DScopy[i] == f:
		DScopy.remove(DScopy[i])
		i -= 1
	i += 1
DScopy.sort()
print(DScopy)
j = 0
while j < len(DS):
	if DS[j] == f:
		DScopy.insert(j,f)
	j += 1 
print(DScopy)

lst = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]

idx = 0
max_idx = len(lst) - 1

max_jdx = len(lst)

while idx < max_idx:
    if lst[idx] == 11:
        idx += 1
        print(idx)
        continue
    jdx = idx + 1
    while jdx < max_jdx:
        if lst[jdx] == 11:
            jdx += 1
            continue
        if lst[idx] > lst[jdx]:
            lst[idx], lst[jdx] = lst[jdx], lst[idx]
        jdx += 1
    idx += 1
print(lst)