def fx(x):
	fx_ = x**3+2*x**2-4*x+1
	return fx_
def bt(lst):
	M_in_fx = []
	M_out_fx = []
	sum_in = 0
	sum_out = 0
	for i in lst:
		if i[1] - fx(i[0]) == 0:
			M_in_fx.append(i)
			sum_in = sum_in + i[1]
		else:
			M_out_fx.append(i)
			sum_out = sum_out + i[1]
	m = abs(sum_in - sum_out)
	return M_in_fx , M_out_fx , m
A = [(-5,-20),(-4,-15),(-3,4),(-2,9),(-1,7),(0,1),(1,-7),(2,-9),(4,81),(5,130)]
print(bt(A))

def bt1(*tup):
	max_ = tup[0]
	for i in tup:
		if max_ < i:
			max_ = i
	return (2*max_ -1)
print(bt1(32,59,8,24,15))
