import math
def area():
    a = int(input("Nhap a : "))
    b = int(input("Nhap b : "))
    c = int(input("Nhap c : "))
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S
print("Dien tich la : ",area())