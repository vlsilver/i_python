#1. map(func, iterable....)
#for i in interable:
	#yield func(x)
vl = lambda x, y: x + y
l_x = [1,2,3,4]
l_y = [1,2,3,4]
a = list(map(vl,l_x,l_y))
print(a)

#2. filter(function or None, iterable)
vl = lambda x: x > 0
vd =(1,2,3,4,-1,-2,-3)
a = list(filter(vl,vd))
print(a)

#3. from functools import reduce
#reduce(function, sequence[, initial])
from functools import reduce
vl = lambda x,y: x*y + 4
vd = (1,2,3,4,5,6)
a = reduce(vl,vd) # ket qua hai so dau thu hien ham voi so tiep theo, neu co initial thi no la gia tri dau tien 
print(a)

#4. Đệ quy

