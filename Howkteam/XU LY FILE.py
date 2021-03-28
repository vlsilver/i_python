F_1=open('vlsilver.txt',mode='r+') #Assign File for Variable open('file name',mode='r/r+/w/w+/a/a+') 
DATA_1=F_1.read() #Read file <File>.read(<number char>), pointer will stay at number char <File>.read(<number char read>)
DATA_2=F_1.read()
F_1.seek(0) #Make pointer come loacation any <File>.seek('Location pointer',set cursor) : 0 cursor at 0, 1 cursor at curent location, -1 cursor end
#F_1.close()
#F_1=open('vlsilver.txt',mode='r+')
DATA_3=F_1.read()
F_1.seek(0)
#F_1.close()
#F_1=open('vlsilver.txt',mode='r+')
DATA_4=F_1.read(22)
DATA_5=F_1.read(40)
F_1.seek(0)
#F_1.close()
#F_1=open('vlsilver.txt',mode='r+')
DATA_6=F_1.readline() #Read a line <File>.readline()
DATA_7=F_1.readline()
F_1.seek(0)
#F_1.close()
#F_1=open('vlsilver.txt',mode='r+')
DATA_8=F_1.readlines() #Get A list with a line is a Element of list attached '\n' <File>.readlines()
F_1.seek(0)
#F_1.close()
#F_1=open('vlsilver.txt',mode='r+')
DATA_9=list(F_1) #Get A list\tuple\set with a line is a Element list\tuple\set(<File>)
DATA_10=F_1.write('\nBE ALONE')#Write new char into File
DATA_11=list(F_1)
print('open("vlsilver.txt",mode="r+")\t=\t',F_1)
print('DATA_1=F_1.read()\t=\t',DATA_1)
print('DATA_2=F_1.read()\t=\t',DATA_2)
print('DATA_3=F_1.read()_after_close->open file\t=\t',DATA_3)
print('DATA_4=F_1.read(22)\t=\t',DATA_4)
print('DATA_5=F_1.read(8)\t=\t',DATA_5)
print('DATA_6=F_1.readline()\t=\t',DATA_6)
print('DATA_7=F_1.readline()\t=\t',DATA_7)
print('DATA_8=F_1.readlines()\t=\t',DATA_8)
print('DATA_9=list(F_1)\t=\t',DATA_9)
print('DATA_10=F_1.write()\t=\t',DATA_10)
with open('vlsilver.txt',mode='r+') as F_2:
	DATA_12=list(F_2)
	print('DATA_12=list(F_2)\t=\t',DATA_12)
 #r: only read
 #r+: read and write at start
 #w: only write
 #w+: write after remove all (makde a file if file nof found) and read
 #a: only write
 #a+: write at end (makde a file if file nof found) and read
 #<file>.tell() : give location of cursor
 #When use write after read ad mode r+, must have seek to set cursor
