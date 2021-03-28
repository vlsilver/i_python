LIST_1=[4,1,2,6,4,1] #make a List (Unhashtable Object)
LIST_2=LIST_1+[] # copy List , ID change
LIST_3=list(LIST_1) #copy List , ID change
LIST_4=LIST_1 #copy List , ID not change
LIST_5=LIST_1.copy() #copy List, ID change
print("LIST_1\t=\t",LIST_1)
print("ID(LIST_1):\t\t",id(LIST_1))
print("LIST_2=LIST_1+[]_ID(LIST_2):\t\t",id(LIST_2))
print("LIST_3=list(LIST_3):\t\t",id(LIST_3))
print("LIST_4=LIST_1:\t\t",id(LIST_4))
print("LIST_5=LIST_1.copy:\t\t",id(LIST_5))

LIST_1+=[1,2] #add List with a List, ID not change
print("\nLIST_1+[1,2]\t=\t",LIST_1)
print("ID(LIST_1):\t\t",id(LIST_1))

print("\nLIST_1[3]\t=\t",LIST_1[1]) #get Element <LIST>[i]
LIST_1[1]=5
print("LIST_1_after_use_LIST1[1]=5\t=\t",LIST_1)
print("LIST_1[::]\t=\t",LIST_1[::]) #get Element to make a List new <LIST>[location get start:location get end:jump] 
print("LIST_1[0:len(LIST_1):2]\t=\t",LIST_1[1:len(LIST_1):2])#get Element to make a List new <LIST>[location get start:location get end:jump]
print("ID(LIST_1):\t\t",id(LIST_1))

LIST_1.reverse() #contrary list <LIST>.reverse()
print("\nLIST_1.reverse()\t=\t",LIST_1)
print("ID(LIST_1):\t\t",id(LIST_1))

LIST_1.sort(reverse=True) #sort list, Type of All Element have sample type <LIST>.sort(reverse = True/False)
print("\nLIST_1.sort()\t=\t",LIST_1)

print('\nLIST_1.count("vlsilver")\t=\t',LIST_1.count("vlsilver")) #count Element <LIST>.count(Element value)
print("ID(LIST_1):\t\t",id(LIST_1))

#print("\nLIST_1.find(2)\t=\t",LIST_1.find(2)) #get location of Element
#print("ID(LIST_1):\t\t",id(LIST_1))

print("\nLIST_1.index(2)\t=\t",LIST_1.index(2)) #get location of Element <LIST>.index(Element value)
print("ID(LIST_1):\t\t",id(LIST_1))

print("\nLIST_1.append([1,2])\t=\t",LIST_1.append([1,2])) #add Object into end LIST <LIST>.append(Object)
LIST_1.extend(['vlsilver','fightting']) #add Object into end LIST <LIST>.append(Object)
print('LIST_1.extend(["vlsilver","fightting"])\t=\t',LIST_1)
LIST_1.insert(len(LIST_1),'fightting')
print("LIST_1.insert('len(LIST_1),'fightting')\t=\t",LIST_1) #add Object into any location of LIST <LIST>.insert(location, Object) 
print("ID(LIST_1):\t\t",id(LIST_1))

print('ELEELEMENT_IN_LOCATION_i=LIST_1.pop(-1)\t=\t',LIST_1.pop(-1))#get Element value choice detele and this element will be deleted of List <LIST>.pop(location element)
print('LIST_1_after_use_LIST1.pop(6)\t=\t',LIST_1)
LIST_1.remove(1)
print('LIST_1.remove(1)\t=\t',LIST_1)#remove Element <LIST>.remove(Element value)
print("ID(LIST_1):\t\t",id(LIST_1))

LIST_1.clear() #detele All Element, get out List empty <LIST>clear()
print('\nLIST_1.clear\t=\t',LIST_1)
print("LIST_2=LIST_1+[]\t=\t",LIST_2)
print("LIST_3=list(LIST_1)\t=\t",LIST_3)
print("LIST_4=LIST_1\t=\t",LIST_4)
print("ID(LIST_1):\t\t",id(LIST_1))
print("ID(LIST_2):\t\t",id(LIST_2))
print("ID(LIST_3):\t\t",id(LIST_3))
print("ID(LIST_4):\t\t",id(LIST_4))


