#iteration, interable
#-Khi bạn tạo  ra một list, bạn có thể truy xuất lần lượt từng giá trị của list đó.
#Người ta gọi đó là iteration
#-list đó là iterable, mọi thứ đều có thể dùng for.....in....... là một interable
#-Tất cả các dữ liệu của iterable sẽ được lưu trữ
print('','iteration-iterable','',sep = '----------')
vl = (0,1,2) #iterable - list, tupple, dict
print(type(vl))
for i in vl:
	print(i,'.....',id(i))
for i in vl:
	print(i,'.....',id(i))
#Generator: for value in .......
#-Là một dạng của iterable gọi là iterator
#-Không lưu trữ tất cả các dữ liệu mà lưu trữ lần lượt
print('','iterator','',sep = '----------')
vl1 = (i for i in range(3))
print(type(vl1)) #iterator
for i in vl1:
	print(i,'...........',id(i))
for i in vl1: # khong ra gi tri
	print('----------------')
	print(i) 

#yield
print('','YIELD','',sep = '----------')
#- Ket qua return la mot object, con yield la mot generator
def yield_(lst):
	lst_new =[]
	for num in lst:
		lst_new.append(num**2)
	yield lst_new
vl = yield_([1,2,3]) #iterator - generator
print(type(vl))
for i in vl:
	print(i)
for i in vl: # khong tao ra gia tri
	print('-----------')
	print(i)
def gen():
	for value in range(3):
		print('yield', value + 1, 'times')
		yield value
for i in gen():
	print(i)
for i in gen(): #chạy thẳng vào hàm
	print(i)
#- Hàm return sẽ ngắt hàm còn yield thì không
#- Hàm yield sẽ chạy tuần tự từ yield này sang yield kia với mỗi lần gọi
def test():
	yield 'Nguyen Vang Linh'
	print('this is the second yield')
	yield 'fighting'
	print('this is the last yield')
	yield 'Handsome'
	print('Will not return anything')
for value in test():
	print(value)
def test1():
 	for i in range(4):
 		yield i
 		yield i**2
test = test1()
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test)) 
#send - generator.send(value) - gán giá trị của generator
print('','SEND','',sep = '----------')
def gen():
	for i in range(4):
		x = yield i
		print('value sent from you', x)
g = gen() # gán generator này cho biến g
print(next(g)) # gọi hàm next để chạy lệnh yield "x = yield i"
g.send('Kteam') # x vừa nãy khi gán cho biến yield giờ sẽ được gửi giá trị
g.send('Free education')
print(next(g)) # lần này ta không dùng send, mặc định giá trị gửi vào là None
print('-----------------------------------------------------------\n-----------------------------')
def test1():
	for i in range(4):
		print('-----------------KHỞI ĐỘNG VÒNG LẶP------------------')
		print('i----->',i)
		print('Tra ra ham YIELD----->',end ='')
		x = yield i*10
		print('x----->',x)
		y = yield x**2
		print('y---->',y)
		yield x**3 , y**2
t = test1()
print(next(t),'\n---------------Kết thúc ở YEILD 1-----------------') #bắt đầu gọi hàm i =0, chạy đến yield 1
print(t.send(5),'\n --------------Kết thúc ở YIELD 2----------------') #gán giá trị cho x = 5, chạy đến yield 2
print(t.send(10),'\n --------------Kết thúc ở YIELD 3-------------------') # gán giá trị cho y =10, chạy đến yield 3
print(next(t),'\n---------------Kết thúc ở YEILD 1-----------------') #bắt đầu gọi hàm i =0, chạy đến yield 1
print(t.send(5),'\n --------------Kết thúc ở YIELD 2----------------') #gán giá trị cho x = 5, chạy đến yield 2
print(t.send(10),'\n --------------Kết thúc ở YIELD 3-------------------') # gán giá trị cho y =10, chạy đến yield 3
