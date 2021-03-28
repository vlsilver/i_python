SET_1={4,1,2,6,4,1}
SET_2=SET_1|{1,2}
SET_3=set(SET_1)
SET_4=SET_1
SET_5=SET_1.copy()
print("SET_1\t=\t",SET_1)
print("ID(SET_1):\t\t",id(SET_1))
print("SET_2=SET_1+[]_ID(SET_2):\t\t",id(SET_2))
print("SET_3=SET(SET_3):\t\t",id(SET_3))
print("SET_4=SET_1:\t\t",id(SET_4))
print("SET_5=SET_1.copy:\t\t",id(SET_5))

#SET_1+={1,2}
#print("\nSET_1+{1,2}\t=\t",SET_1)
#print("ID(SET_1):\t\t",id(SET_1))

#print("\nSET_1[3]\t=\t",SET_1[1])
#SET_1[1]=5
#print("SET_1_after_use_SET_1[1]=5\t=\t",SET_1)
#print("SET_1[::]\t=\t",SET_1[::])
#print("SET_1[0:len(SET_1):2]\t=\t",SET_1[1:len(SET_1):2])
#print("ID(SET_1):\t\t",id(SET_1))

#SET_1.reverse()
#print("\nSET_1.reverse()\t=\t",SET_1)
#print("ID(SET_1):\t\t",id(SET_1))

#SET_1.sort() # ELenemrnt of SET sample type
#print("\nSET_1.sort()\t=\t",SET_1)

#print('\nSET_1.count("vlsilver"):\t\t',SET_1.count("vlsilver"))
#print("ID(SET_1):\t\t",id(SET_1))

#print("\nSET_1.index(2)\t=\t",SET_1.index(2))
#print("ID(SET_1):\t\t",id(SET_1))

#print("\nSET_1.append([1,2])\t=\t",SET_1.append([1,2]))
#SET_1.extend(['vlsilver','fightting'])
#print('SET_1.extend(["vlsilver","fightting"]):\t=\t',SET_1)
#print("ID(SET_1):\t\t",id(SET_1))

#SET_1.insert(len(SET_1),'fightting')
#print("\nSET_1.insert('len(SET_1),'fightting')\t\t",SET_1)
#print("ID(SET_1):\t\t",id(SET_1))

print('\nELEMENT_IN_LOCATION_i=SET_1.pop()\t=\t',SET_1.pop()) #remove the first Element of Set <set>.pop()
print('SET_1_after_use_SET1.pop()\t=\t',SET_1)
SET_1.remove(2) #remove Element of set, if set don't have element removed, get error <set>.remove(element value)
print('SET_1.remove(2)\t=\t',SET_1)
SET_1.discard(4) #remove element of set <set>.discard(element value)
print('SET_1.discard(4)\t=\t',SET_1)
print("ID(SET_1):\t\t",id(SET_1))

SET_1.clear() #remove all Elemrnt of SET
print('\nSET_1.clear\t=\t',SET_1)

print('\nSET_1\t=\t',SET_1)
print("SET_2=SET_1|{1,2}\t=\t",SET_2)
print("SET_3=SET(SET_1)\t=\t",SET_3)
print("SET_4=SET_1\t=\t",SET_4)

print("\nID(SET_1):\t\t",id(SET_1))
print("ID(SET_2):\t\t",id(SET_2))
print("ID(SET_3):\t\t",id(SET_3))
print("ID(SET_4):\t\t",id(SET_4))
