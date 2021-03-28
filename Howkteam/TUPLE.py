TUP_1=(4,1,2,6,4,1,'vlsilver',(1,2),[1,2])
TUP_2=TUP_1+()
TUP_3=tuple(TUP_1)
TUP_4=TUP_1
#TUP_5=TUP_1.copy()
print("TUP_1\t=\t",TUP_1)
print("ID(TUP_1):\t\t",id(TUP_1))
print("TUP_2=TUP_1+[]_ID(TUP_2):\t\t",id(TUP_2))
print("TUP_3=tuple(TUP_1):\t\t",id(TUP_3))
print("TUP_4=TUP_1:\t\t",id(TUP_4))
#print('TUP_5=TUP_1.copy()',id(TUP_5))

TUP_1+=(1,2) #make a new tuple, change ID
print("\nTUP_1+=[1,2]\t=\t",TUP_1)
print("ID(TUP_1):\t\t",id(TUP_1))

print("\nTUP_1[3]\t=\t",TUP_1[1]) #get Element <Tuple>[location Element]
#TUP_1[1]=5
#print("TUP_1_after_use_TUP_1[1]=5\t=\t",TUP_1)
print("TUP_1[::]\t=\t",TUP_1[::]) #make a new tuple, get some Element of Tuple old <tuple>[loacation get start:location get end:jump]
print("TUP_1[0:len(TUP_1):2]\t=\t",TUP_1[1:len(TUP_1):2])
print("ID(TUP_1):\t\t",id(TUP_1))

#TUP_1.reverse()
#print("\nTUP_1.reverse()\t=\t",TUP_1)
#print("ID(TUP_1):\t\t",id(TUP_1))

#TUP_1.sort() # ELenemrnt of TUP sample type
#print("\nTUP_1.sort()\t=\t",TUP_1)

print('\nTUP_1.count("vlsilver"):\t\t',TUP_1.count("vlsilver")) #count Element of tuple <tuple>.count(Element value)
print("ID(TUP_1):\t\t",id(TUP_1))

print("\nTUP_1.index(2)\t=\t",TUP_1.index(2)) #get location Element is first founded of tuple <tuple>.index(Element value)
print("ID(TUP_1):\t\t",id(TUP_1))

#print("\nTUP_1.append([1,2])\t=\t",TUP_1.append([1,2]))
#TUP_1.extend(['vlsilver','fightting'])
#print('TUP_1.extend(["vlsilver","fightting"]):\t=\t',TUP_1)
#print("ID(TUP_1):\t\t",id(TUP_1))

#TUP_1.insert(len(TUP_1),'fightting')
#print("\nTUP_1.insert('len(TUP_1),'fightting')\t\t",TUP_1)
#print("ID(TUP_1):\t\t",id(TUP_1))

#print('\nELEMENT_IN_LOCATION_i=TUP_1.pop(-1)\t=\t',TUP_1.pop(-1))
#print('TUP_1_after_use_TUP1.pop(6)\t=\t',TUP_1)
#TUP_1.remove(1)
#print('TUP_1.remove(1)\t=\t',TUP_1)
#print("ID(TUP_1):\t\t",id(TUP_1))

#TUP_1.clear()
#print('\nTUP_1.clear\t=\t',TUP_1)
#print('\nTUP_1.clear\t=\t',TUP_1)
print("TUP_1\t=\t",TUP_1)
print("TUP_2=TUP_1+()\t=\t",TUP_2)
print("TUP_3=tuple(TUP_1)\t=\t",TUP_3)
print("TUP_4=TUP_1\t=\t",TUP_4)
print("ID(TUP_1):\t\t",id(TUP_1))
print("ID(TUP_2):\t\t",id(TUP_2))
print("ID(TUP_3):\t\t",id(TUP_3))
print("ID(TUP_4):\t\t",id(TUP_4))



