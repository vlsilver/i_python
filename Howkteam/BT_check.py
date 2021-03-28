		
def max_k(lst_k):
	max_k = lst_k[0]
	idex_k = 0
	for i in range(len(lst_k)):
		if lst_k[i] >= max_k:
			max_k = lst_k[i]
			idex_k = i
	return max_k, idex_k
def top_min_k(lst,k):
	top_min_k = lst[0:k]
	mx = 0
	ix = 0
	for i in range(k,len(lst)):
		mx, ix = max_k(top_min_k)
		if mx > lst[i]:
			top_min_k[ix] = lst[i]
	return top_min_k
print(top_min_k([-120,-120,-120,-0,-12091,-100,1,6,5,-100,3,-100,-101],3))