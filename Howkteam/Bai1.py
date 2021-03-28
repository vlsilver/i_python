# Print screen Name Project
print("{:-^100}".format("VLSILVER PROJECT"))
# Get Variable x,y,z
x=int(3)
y=float(1.111)
#ADD/import All "decimal" library
from decimal import*#add/import All "decimal" library from " Library" import*
getcontext().prec=30
z=Decimal(10)/3
#ADD/import All "fractions" library 
from fractions import*
v=Fraction(6,9) 
u=complex(1,2)

#print screen value of Varialbe
print("{:-^100}".format("XUAT GIA TRI BIEN"))
print(x)
print(y)
print(z)
print(v)
print(u), print(u.real), print(u.imag)

# Print screen type of variable "x,y,t,z"
print("\n{:-^100}".format("KIEU DU LIEU CUA BIEN")) 
print(type(x))
print(type(y))
print(type(z))
print(type(v))
print(type(u))

print("\n{:-^100}".format("CAC PHEP TOAN DAC BIET"))
print(5//3)#Chia lay nguyen
print(5%3)#Chia lay du
print(5**2)#luy thua 5^2
#ADD/import "MATCH" library

print("\n{:-^100}".format("CAC HAM TOAN DAC BIET"))
import math
print(math.trunc(3.14))#Lay so nguyen
print(math.floor(4.9999999))#Lam tron xuong
print(math.ceil(4.9999999999))#Lam tron len
print(math.fabs(-4.14))#Gia tri tuyet doi
print(math.sqrt(4.14))#Can bac hai
print(math.gcd(4,8))#Uoc chung lon nhat

print("\n{:-^100}".format("CHUOI CO BAN"))
strA_0=str("VL'SILVER")
strA_1=str('VL"SILVER')
strA_2=str("VL_SILVER\nFIGHTING\nFIGHTING")
print(strA_0)
print(strA_1)
print(strA_2)
print("\a")#tao 1 tieng bip
print("VL_SILVEE\bR")#dua con tro ve lai mot khoang trang
print("VL_SILBVER\tFIGHT")#tab
print("\'")#tao ra '
print("\"")#tao ra "

print("\n{:-^100}".format("XU LY CHUOI"))
strB_0=str(r"V\LSILVER")#bo chuc nang cua \
strB_1=str("FIGHTING")
strB_2=strA_0+"\t"+strB_1
strB_3=strA_0+"\t"+strB_1*5
strB_4=strA_0 in strB_3#"strA_0" co trong "strB_3" khong?
strB_5=strB_0[0]
strB_6=strB_0[len(strB_0)-1]
strB_7=strB_0[0:6]
strB_8=strB_0[None:None:2]#Buoc nhay la 2
strB_9=strB_0[0:1]+""+strB_0[2:None]#Doi ky tu \
print(strB_0)
print(strB_2)
print(strB_3)
print(strB_4)
print(strB_5)
print(strB_6)
print(strB_7)
print(strB_8)
print(strB_9)

print("\n{:-^100}".format("DINH DANG CHUOI"))
strC_0=str("VLSIVER %s %s"%("FIGHTING","THE FIRST DAY"))#lay ky tu thay vao %s
strC_1="%r"%(2)
strC_2="%d"%(2.1)#lay phan nguyen thay vao chuoi %d
strC_3="%.5f" %(2.2222)#Layso thuc thay vao chuoi %.5f
strC_4=f"{strB_9} FIGHTING"#thay the bien bang gia tri cua no trong chuoi 
strC_5=f"{{strB_10}} {strB_9} {strB_1}"#thay the bien bang gia tri cua no trong chuoi 
strC_6="a:{x_0} b:{y_0} c:{z_0}".format(x_0=1,y_0=2,z_0=3)#thay the theo ap dat gia tri bien
strC_7="a:{2} b:{1} c:{0}".format(0,1,2)#thay the thei STT
strC_8="a:{} b:{} c:{}".format(1,2,3)#replace objects outside in function format for strings {<i>,<variable>,<>} "{}".format(objects_i)
strC_9="{:*^50}".format('VLSIVER')#Align center string "{:"char align"^number align}.format(str align)"
strC_10="{:*>50}".format("VLSIVER")#Align right string "{:"char align">number align}.format(str align)"
strC_11="{:*<50}".format("VLSIVER")#Align left string "{:"char align"<number align}".format(str align)
ten_1="NGUYEN VANG LINH"
SDT_1="0979695618"
BD_1="06/06/1994"
row_1="{:*^94}".format("")
row_2="|{:<30}|{:^30}|{:>30}|".format("NAME","PHONE NUMBER","BITHDAY")
row_3="|{:<30}|{:^30}|{:>30}|".format(ten_1,SDT_1,BD_1)
row_4="{:*<94}".format("")
print(strC_1)
print(strC_2)
print(strC_3)
print(strC_4)
print(strC_5)
print(strC_6)
print(strC_7)
print(strC_8)
print(strC_9)
print(strC_10)
print(strC_11)
print(row_1)
print(row_2)
print(row_3)
print(row_4)

print("\n{:-^100}".format("PHUONG THUC CHUOI 1"))
strD_0="vlsilver fighting"
strD_1=strD_0.capitalize()#get upper the char start of string str.capitalize()
strD_2=strD_0.upper()#get upper all the char of string str.upper()
strD_3=strD_0.lower()#get lower all the char of string str.lower()
strD_4=strD_0.title()#get title all the str before the space of string str.title()
strD_5=strD_4.center(100,"*")#Align center string str.center(range align,"char align")
strD_6=strD_4.rjust(100,"*")# Align right string str.rjust(range align, "char align")
strD_7=strD_4.ljust(100,"*")#Align left string str.ljust(range align,"char align")
strD_8=strD_4.encode(encoding="utf-8",errors="strict")# encode string ( study avandce after) str.encode(??????)
strD_9=strD_4.join(["1","2","3"])#join string with str str.join(list join) 1+str+2+str+3
strD_10=strD_4.replace("Vl","_",1)#replace str old in string for str new str.replace("str old","str new",number str old is replaced)
strD_11=strD_4.strip("V")#cut str in rear string and head string str.strip("str cut"), if char of str cuting in string, it is cuted. 
strD_12=strD_4.rstrip("g")
strD_13=strD_4.lstrip("V")
print(strD_1)
print(strD_2)
print(strD_3)
print(strD_4)
print(strD_5)
print(strD_6)
print(strD_7)
print(strD_8)
print(strD_9)
print(strD_10)
print(strD_11)
print(strD_12)
print(strD_13)

print("\n{:-^100}".format("PHUONG THUC CHUOI 2"))
strE_0="fighting vlsilver fighting"
strE_1=strE_0.split("v",1)#cut string to create list str.split("str cut",number cut) str cut in not list.
strE_2=strE_0.split("v",2)
strE_3=strE_0.rsplit(" ",1) 
strE_4=strE_0.partition("vlsilver")#create list with three string, str 1 is string cuting before, str 3 is str cuting after, str 2 is str cuting str.partition("str cut")
strE_5=strE_0.count("vl",0,len(strE_0))#count str in stringstr.count("str count",(location start count),(location end count)) - location count not need. 
strE_6=strE_0.startswith("vl",0,len(strE_0))# check str in starts string? str.startswith("str check",(location starts check),(location end check)) - location check not need
strE_7=strE_0.endswith("ing",0,len(strE_0))
strE_8=strE_0.find("vl",0,None)#find location str in string, if function cannot find it, get number -1 str.find("find str",(location start find),(location end start))-location find not need
strE_9=strE_0.index("f")#sameple function find, however if function cannot find it, get error
strE_10=strE_0.islower()#check str is lower string? str.islower
strE_11=strE_0.istitle()#check str is title string? str.istitle
strE_12=strE_0.isdigit()#check str is digit? str.isdigit
strE_13=strE_0.isspace()#Check str cover all space? str.isspace
print(strE_1)
print(strE_2)
print(strE_3)
print(strE_4)
print(strE_5)
print(strE_6)
print(strE_7)
print(strE_8)
print(strE_9)
print(strE_10)
print(strE_11)
print(strE_12)
print(strE_13)

print("\n{:-^100}".format("KIEU DU LIEU MANG"))
print("{:*<100}".format("KHAI BAO MANG"))
Name="Nguyen Vang Linh"
Age=27
PhoneNumber="0979695618"
A=[Name,Age,PhoneNumber]
A_0=list(A) #If A[i] change and A[i] is not list , A_0[i] not change, It is not B=A list(list/string(get array all char in string )")
A_1=[i for i in range(30)]#
A_2=[[i,i*3,i*4] for i in range(0,3)]
A_2.reverse()
print(A)
print(A_0)
print(A_1)
print("A_2\t=\t",A_2)
print("{:*<100}".format("CAC PHUONG THUC VOI LIST"))
B_1=len(A_1)#check len of list/string len(list/string)
B_2=1 in A#check object in list/string <Object> in <Object(string/list)>
B_3=A_0[0:None:2]#get Elements of string/List <String/List>[location get start:location get end]
B_4=A.count(A[0])#check amuont object in List <List>.count(<Object>)
B_5=A.index(A[0])#find object in List, get location of object <List>.index(<Object>)
B_6=A.copy()#Copy List, If List old change, List new not change B <List>.copy()
A_1.clear()# Clear All Elements of List <List>.Clear() 
A.append([4,5])#Add object into List <List>.append(<Object>)
A.extend([1,2,3,["vlsilver"]])#Add object into List, if Object is a List, Function Extend will add Element of List into List old <List>.extend(<Object...>) 
A.insert(0,[1,2,3])#Insert Object into List equal loacation <List>.insert(location,<Object>) 
B_7=A#if List Old change, List new change and contrary
print("A\t=\t", A)
B_8=A.pop()#Remove Element of List equal location Element and get Element Delete <List>.pop(location Element)
A.remove([1,2,3])#Remove Element first of List is founded <List>.remove(Element remove) 
A.reverse()#contrary List <List>.reverse()
A_2.sort()#Sort List, All Element of List sample type <List>.sort()
A_2.sort(reverse=True)#Sort List with contrary <List>.sort(reverse=True/False) 
print(B_1)
print(B_2)
print("B_3\t=\t", B_3)
print("B_4\t=\t", B_4)
print("B_5\t=\t", B_5)
print("B_6\t=\t", B_6)
print("A_1\t=\t", A_1)
print("A\t=\t", A)
print("B_7\t=\t", B_7)
print("B_8\t=\t", B_8)
print("A_2\t=\t", A_2)

print("\n{:-^100}".format("KIEU DU LIEU TUPLE"))
print("{:*<100}".format("KHAI BAO TUPLE"))
TUP=(Name,Age,PhoneNumber)
TUP_1=(i for i in range(8) if i%2==0)
TUP_2=tuple(TUP_1)
TUP_3=tuple((1,2,3))
print("TUP\t=\t",TUP)
print("TUP_1\t=\t",TUP_1)
print("TUP_2\t=\t",TUP_2)
print("TUP_3\t=\t",TUP_3)
print("{:*<100}".format("CAC PHUONG THUC VOI TUPLE"))
TUP_4=TUP_2+TUP_3
TUP_5=TUP_4[0:3:2]#get Element of tuple <tuple>[location start get:location end sget:jump]
print("TUP_4\t=\t",TUP_4)
print("TUP_5\t=\t",TUP_5)
print("\n{:-^100}".format("SO SANH HASHALBE VA UNHASABLE"))
#List: Unhashable - ID will not change when you use function - When create hasable object Pyhthon program will use data memory more than necessary.
#String, Tuple: Hashable - ID will change when you use function - When create unhasable object Python program will use data memory just enough.
STR="vlsilver"
print("ID STR:\t\t",id(STR))
STR+="fighting"
print("ID STR:\t\t",id(STR))
TUP=("vlsilver",1)
print("ID TUP:\t\t",id(TUP))
TUP+=("fighting",)
print("ID TUP:\t\t",id(TUP))
LST=["vlsilver",1]
print("ID LST:\t\t",id(LST))
LST.append("fighting")
#LST+=["fighting"]
print("ID LST:\t\t",id(LST))
print("\n{:-^100}".format("KIEU DU LIEU SET"))
SET_1={(1,2,3),1,1,2}#Not Contain Unhashable Object(List), If Data contain Element sample, SET only once contain Element.  
SET_2=set(i*2 for i in range(3))# <variable> for <variable> range(<:>)
SET_3=SET_1 in SET_2
SET_4=SET_2-SET_1
SET_5=SET_1&SET_2
SET_6=SET_1|SET_2
SET_7=SET_1^SET_2
print("SET_1\t=\t",SET_1)
print("SET_2\t=\t",SET_2)
print("SET_3\t=\t",SET_3)
print("SET_4\t=\t",SET_4)
print("SET_5\t=\t",SET_5)
print("SET_6\t=\t",SET_6)
print("SET_7\t=\t",SET_7)
SET_7.clear()#clear set <SET>.clear()
SET_6.pop()#remove Element of the fisrt of set <SET>.pop()
SET_5.remove(2)#remove Element of set, if not founded Element remove, get error <SET>.remove(<value of Element>)
SET_4.discard(3)#remove Element of set, if nor founed Element remove, keep on <SET>.discard(<value of Element>)
print("SET_7.clear()\t=\t",SET_7)
print("SET_6.pop()\t=\t",SET_6)
print("SET_5.remove\t=\t",SET_5)
print("SET_4.discard\t=\t",SET_4)
SET_8=SET_4.copy()|{"vlsilver"}
print("SET_8=SET_5.copy()\t=\t",SET_8)

