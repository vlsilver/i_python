print("\n{:-^100}".format("THUC HANH"))

print("\n{:-^100}".format("DINH DANG SO TRONG PYTHON"))
x=2+0j#x=comple(2,0)
y=4.1224
z=3
from decimal import*	#Import thu vien decimal
getcontext().prec=10	#Quy dinh so chu so cua Decimal
t=Decimal(10)/3
print("Day la so Phuc:\t",x)
print("Day la phan thuc cua so phuc:\t",x.real)
print("Day la phan ao cua so phuc:\t",x.imag)
print("Day la kieu du lieu cua bien x-so phuc:\t",x,type(x))
print("Day la kieu du lieu cua bien y-so thuc:\t",y,type(y))
print("Day la kieu du lieu cua bien z-so nguyen:\t",z,type(z))
print("Day la kieu du lieu cua bien t-Decimal:\t",t,type(t))
print("\n{:-^100}".format("PHEP TOAN SO HOC"))
import math
print("\n{:-^100}".format("DINH DANG CHUOI TRONG PYTHON"))
s1="Nguyen Vang Linh"
s2="0979695618"
s3="06/06/1994"
a="Day la dinh dang %s %s " %(r"Lay chuoi %s","theo phuong thuc xuat str")
b="Day la dinh dang %r %r"%(r"Lay chuoi %r","theo phuong thuc rept")
c="Day la dinh dang lay so nguyen d1=%d; d2=%d"%(3.41,4.12)
d="Day la dinh dang lay so thuc f1=%.5f; f2=%.1f"%(3.41414,5.1251252)
e=f"Day la dinh dang lay chuoi f-Name:{s1}\tPhoneNumber:{s2}\tBithDay:{s3}"
f_1="Day la dinh dang chuoi Format_0-Name:{}\tPhoneNumber:{}\tBithDay{}".format(s1,s2,s3)
f_2="Day la dinh dang chuoi Format_1-Name:{2}\tPhoneNumber:{1}\tBithDay{0}".format(s3,s2,s1)
f_3="Day la dinh dang chuoi Format_2-Name:{:<10}PhoneNumber{:^30}BithDay:{:>10}".format(s3,s2,s1)
f_4="|{:*<30}|{:*^30}|{:*>30}|".format("","","",)+"\n|{:<30}|{:<30}|{:<30}|".format(s1,s2,s3)+"\n|{:*<30}|{:*<30}|{:*<30}|".format("","","")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f_1)
print(f_2)
print(f_3)
print(f_4)
print("\n{:-^100}".format("XU LY CHUOI"))
s="aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa"
s0=((s.strip("aaaAAaaaooaa"))+"o").title()
s1=s[s.find("n"):s.find("D")+2].title()
a= "rrrrr"
print(s0)
print(s1)
print("{:-^100}".format("BAI TAP VE MANG"))
A_1 = ["list(list(list('abc'))"]
A_2 =["list()"]
print("A_1\t=\t",A_1)
print("A_2\t=\t",A_2)
s='aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
s_0= s[s.find("&&")+2:s.find("%%")]
s_1 = s.split("&&")[-1].split("%%")[0]
print("key can tim la:\t\t",s_0)
print("key can tim la:\t\t",s_1)