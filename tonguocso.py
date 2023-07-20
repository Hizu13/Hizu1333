import math
n = int(input("N = "))
s=0
for i in range (1,int(math.sqrt(n)+1)):
    if(n%(i)==0):
        s=s+i
        if(n//i != i):
            s += n//i
print("Tong cac uoc so cua %d la %d" %(n,s))