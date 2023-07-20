import math
def area2():
    print("Toa do diem A la : ")
    x1 = int(input("x = "))
    y1 = int(input("y = "))
    print("Toa do diem B la : ")
    x2 = int(input("x = "))
    y2 = int(input("y = "))
    print("Toa do diem C la : ")
    x3 = int(input("x = "))
    y3 = int(input("y = "))
    AB = math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
    BC = math.sqrt(pow((x2-x3),2)+pow((y2-y3),2))
    AC = math.sqrt(pow((x1-x3),2)+pow((y1-y3),2))
    p = (AB + BC + AC) / 2
    S = math.sqrt(p*(p-AB)*(p-BC)*(p-AC))
    print("Dien tich tam giac la : ",S)
area2()