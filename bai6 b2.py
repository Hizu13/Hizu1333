def giaiThua(N):
    Giaithua = 1
    for i in range(1,N+1):
        Giaithua = Giaithua * i
    return Giaithua
# print(giaiThua(N))

N = int(input("Nhap N = "))
s=0
for i in range(1, N+1):
    s = s + giaiThua(i)

print(s)
