#lambda dùng để khai báo hàm
#lambda argument..............: expression
vl = lambda name, birthday, age : [name, birthday, age]
print(vl('Nguyen Vang Linh','6/6/1994',27))

def thongtin():
	vl = lambda name, birthday, age : [name, birthday, age]
	return vl
call_vl = thongtin()
print(call_vl('Nguyen Vang Linh','6/6/1994',27))

thongtin = [lambda x: x**3, lambda x: x*3, lambda x: x*2]
print(thongtin[1](2))
print(thongtin[2](4))
for y in thongtin:
	print(y(4))

key = 'Nguyen Vang Linh'
print({'Nguyen Vang Linh':lambda:"1994"}[key]())

dic = {'Linh':1994, 'Trinh': 1994}
for i in dic.keys():
	print(dic[i])

dk = lambda x: 'Boi cua 3,2' if not (x % 3 != 0) and not (x % 2 ) != 0 else 'Khong phai boi cua 3,2'
print(dk(6))

def thongtin(name):
	return lambda birthday: name + birthday
a = thongtin('Nguyen Vang Linh')
print(a('6/6/1994'))