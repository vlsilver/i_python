DICT_1={'Name':'Nguyen Vang Linh','Age':27,'PhoneNumber':'0979695618'} #make a DICT, key have might hasable object  {key:value,....}
DICT_1_1={key:value for key, value in (('Name','Nguyen Vang Linh'),('Age',27),('PhoneNumber','0979695618')) } 
DICT_1_2={('Name','Nguyen Vang Linh'),('Age',27),('PhoneNumber','0979695618')}
DICT_1_3=dict(Name='Nguyen Vang Linh',Age=27,PhoneNumber='0979695618')
thongtin=('Name','Age','PhoneNumber')
DICT_1_4=dict.fromkeys(thongtin,'Nguyen Vang Linh') 
#DICT_2=DICT_1+{} # copy DICT , ID change
DICT_3=dict(DICT_1) #copy DICT , ID change
DICT_4=DICT_1#copy DICT , ID not change
DICT_5=DICT_1.copy() #copy DICT, ID change
print("DICT_1\t=\t",DICT_1)
print("DICT_1_1\t=\t",DICT_1_1)
print("DICT_1_2\t=\t",DICT_1_2)
print("DICT_1_3\t=\t",DICT_1_3)
print("DICT_1_4\t=\t",DICT_1_4)
print("DICT_3\t=\t",DICT_3)
print("ID(DICT_1):\t\t",id(DICT_1))
#print("DICT_=DICT_1+[]_ID(DICT_2):\t\t",id(DICT_2))
print("DICT_3=dict(DICT_3):\t\t",id(DICT_3))
print("DICT_4=DICT_1:\t\t",id(DICT_4))
print("DICT_5=DICT_1.copy:\t\t",id(DICT_5))


#DICT_1+={'BithDay:'6/6/1994'} #add DICT with a DICT, ID not change
#print("\nDICT_1+[1,2]\t=\t",DICT_1)
#print("ID(DICT_1):\t\t",id(DICT_1))

print("\nDICT_1[Name]\t=\t",DICT_1['Name']) #get Element value, if key not is in DICT, get error <DICT>[key]
print("DICT_1.get('Like','Key not be founded')\t=\t",DICT_1.get('Like','Key not be founded')) #get Element value, if key not is in DICT, get 'value other' <DICT>.get(key,value other)
DICT_1['Name']='vlsilver' #change value of key, <DICT>[key]=<new value>
print("DICT_1_after_use_DICT1['Name']='vlsilver'\t=\t",DICT_1)
DICT_1['BithDay']='6/6/1994' #change value of key, if key not in DICT, DICT will add this key, value into it <DICT>[new key]=value
print("DICT_1_after_use_DICT1['BithDay']='6/6/1994'\t=\t",DICT_1)
print("DICT_1.setdefault('BithDay')\t=\t",DICT_1.setdefault('Like','CODE')) #get value of key, if key not be founded, this key and value will be add into DICT <DICT>.setdefault('key check',value new) 
print("DICT_1_after_use_DICT1.setdefault('Like','CODE')\t=\t",DICT_1)
print("DICT_1.item()\t=\t",DICT_1.items(),"\nTEPY(DICT_1.items()):\t\t",type(DICT_1.items()))#get a dict_items class object <DICT>.items()
print("DICT_1.key()\t=\t",DICT_1.keys()) #get menu all key <DICT>.keys()
print("DICT_1.values()\t=\t",DICT_1.values()) #get menu all values <DICT>.values()
#print("DICT_1[::]\t=\t",DICT_1[::]) #get Element to make a DICT new <DICT>[location get start:location get end:jump] 
#print("DICT_1[0:len(DICT_1):2]\t=\t",DICT_1[1:len(DICT_1):2])#get Element to make a DICT new <DICT>[location get start:location get end:jump]
print("ID(DICT_1):\t\t",id(DICT_1))



#DICT_1.reverse() #contrary DICT <DICT>.reverse()
#print("\nDICT_1.reverse()\t=\t",DICT_1)
#print("ID(DICT_1):\t\t",id(DICT_1))

#DICT_1.sort(reverse=True) #sort DICT, Type of All Element have sample type <DICT>.sort(reverse = True/False)
#print("\nDICT_1.sort()\t=\t",DICT_1)

#print('\nDICT_1.count("vlsilver")\t=\t',DICT_1.count("vlsilver")) #count Element <DICT>.count(Element value)
#print("ID(DICT_1):\t\t",id(DICT_1))

#print("\nDICT_1.find(2)\t=\t",DICT_1.find(2)) #get location of Element
#print("ID(DICT_1):\t\t",id(DICT_1))

#print("\nDICT_1.index(2)\t=\t",DICT_1.index(2)) #get location of Element <DICT>.index(Element value)
#print("ID(DICT_1):\t\t",id(DICT_1))

#print("\nDICT_1.append([1,2])\t=\t",DICT_1.append([1,2])) #add Object into end DICT <DICT>.append(Object)
#DICT_1.extend(['vlsilver','fightting']) #add Object into end DICT <DICT>.append(Object)
#print('DICT_1.extend(["vlsilver","fightting"])\t=\t',DICT_1)
#DICT_1.insert(len(DICT_1),'fightting')
#print("DICT_1.insert('len(DICT_1),'fightting')\t=\t",DICT_1) #add Object into any location of DICT <DICT>.insert(location, Object) 
#print("ID(DICT_1):\t\t",id(DICT_1))

print('\nValue_of_Key_POP=DICT_1.pop("Like","Key not be founded")\t=\t',DICT_1.pop('Like','Key not be founded'))#get Element key choice detele and this element will be deleted of DICT <DICT>.pop(key,"other value if key not be founded")
print('DICT_1_after_use_DICT_1.pop("Like","Key not be founded")\t=\t',DICT_1)
print('Value_of_Key_POP=DICT_1.popitem()\t=\t',DICT_1.popitem())#get Element(key,value) random and remmove Element this, iF DICT is None, get error <DICT_1>.popitem()
print('DICT_1_after_use_DICT_1.popitem()\t=\t',DICT_1)
#DICT_1.remove(1)
#print('DICT_1.remove(1)\t=\t',DICT_1)#remove Element <DICT>.remove(Element value)
print("ID(DICT_1):\t\t",id(DICT_1))

DICT_1.update(Name='Nguyen Vang Linh',Age=28)#Update value for ket or add (new key, new value) into Dict <Dict>.update(key=value,....)
print('DICT_1_after_use_DICT_1.update("Name":"Nguyen Vang Linh")\t=\t',DICT_1)
print("ID(DICT_1):\t\t",id(DICT_1))

DICT_1.clear() #detele All Element, get out DICT empty <DICT>clear()
print('\nDICT_1.clear\t=\t',DICT_1)
#print("DICT_2=DICT_1+[]\t=\t",DICT_2)
print("DICT_3=DICT(DICT_1)\t=\t",DICT_3)
print("DICT_4=DICT_1\t=\t",DICT_4)
print("ID(DICT_1):\t\t",id(DICT_1))
#print("ID(DICT_2):\t\t",id(DICT_2))
print("ID(DICT_3):\t\t",id(DICT_3))
print("ID(DICT_4):\t\t",id(DICT_4))


