n = int(input("Nhap N duong: "))
tong = 1
giaithua = 0

for i in range(1,n+1):
    tong*i = tong
    giaithua = giaithua + tong
    # print(giaithua)

    
print(f"F({n}) = {giaithua}")