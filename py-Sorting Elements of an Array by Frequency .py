def sortByFred(a,n):
	a.sort()
	a_count = []
	a_sort =[]
	for i in a:
		a_count.append(a.count(i))
	for i in range(len(a)):
		max_ = max(a_count)
		k = a_count.index(max_)
		a_count.pop(k)
		a_sort.append(a[k])
		a.pop(k)
	return a_sort
print(sortByFred([9,9,2,2,9,10,10,10,6,6,6,6,6,15,15,15,1,15,15,21,-6,-6,-6,2,2,2,-3,15,-6,-6-4,-4,-4,3,3,3,2,2],5))


