print('','FUNCTION GET OUT "PRINT" IN PYTHON','',sep = '------------------')
#print(object,sep = '',end = '\n',file = sys.stdout,flush = false)
print('','NGUYEN VANG LINH','',sep = '---------',end = '++++')
print('6/6/1994')
from time import sleep
ten = 'NGUYEN VANG LINH'
namsinh = '6/6/1994'
for i in ten:
	if ten.index(i) != len(ten)-1:
		print(i,end = '',flush = True)
		sleep(0.1)
	else:
		print(i)		
		sleep(0.1)
with open('vlsilver.txt','r+') as f:
	print('Ten:\t',ten,'\nNam sinh:\t',namsinh,file = f) #if file not find, it make new file
#print('','NGUYEN VANG LINH','',sep = '---------',end = '++++';flush = True)