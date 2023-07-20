def total():
    N = int(input("Nhap N = "))
    s = 0
    while N!=0 :
        s += N%10
        N //= 10
    print("Tong cac chu so la",s)
total()
