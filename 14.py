import math
n = int(input("N = "))
s = 0
y=1
# y = math.pow(2,n)
for i in range(0,n):
    y = y*2
while y!=0 :
        s += y%10
        y //= 10

        
print("Tong =",int(s))
