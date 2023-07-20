def ktsn(n):
    try:
        n = int(n)
        return True
    except:
        return False
def ktsothuc(n):
    try:
        
        n = float(n)
        return True
    except:
        return False
a = []
b = []
c = []
tong = 0
tong2 = 0
tong1=0

n = int(input("Nhap N: "))
for i in range(1,n+1):
    t = input(f"Nhap gia tri thu {i}: ")
    if(ktsn(t)):           
            a.append(int(t))
            tong1 = tong1 + int(t)        
    elif(ktsothuc(t)):
            
        b.append(float(t))
        tong2 = tong2 + float(t)
    else: c.append(t)
tong = tong1+tong2
x = len(a)
y = len(b)

if(x == 0 and y == 0):
    print("B =",c)
else:
    print("TBC cua A =" ,tong/(x+y))
    print("B =",c)
