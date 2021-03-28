# def <function name>(parameter........)
def vd(age, ten = "Nguyen Vang Linh"):
 	print(age)
 	print(ten)
 	return
vd(27, 'V.T.V.T')
vd(27)
print('','Positional argument and keyword argument','',sep = '-----------------')
def vd2(text, lst =[]):
	lst.append(text)
	print(lst)
vd2('VNL',[1]) #( gia tri truyen vao la Positional argument)
vd2('Love')
vd2('VTVT')
vd2(text = 'Haha') # (gia tri truyen vao duoi dang keyword argument)
def vd3(age,*,Namsinh,ten): #(Namsinh va ten phai duoc truyen duoi dang keyword agrument - keword only argument) (parameter,\ - parameter is positional only argument ) 
	print(Namsinh)
	print(ten)
vd3(27, Namsinh = 1994,ten = "NVL")
print('','Unpacking - Packing','',sep = '------------------------')
def vd3(name,age,namsinh,):
	print(name,age,namsinh)
dic = {'age':27,'namsinh':1994}
print(vd3(*['NVL',27,1994])) # unpaking
print(vd3('NVL',**dic))
def vd4(**args):
	print(args)
print(vd4(age = 27, namsinh = 1994, name = 'NVL'))
def vd5(*args,name):
	print(args)
	print(name)
print(vd5(*(x for x in range(10)),name = 'NVL'))

