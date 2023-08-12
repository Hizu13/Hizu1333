sanpham = ['pear', 'orange', 'apple', 'banana']
gia = [3, 1.5, 2, 4]
soluong = []
print("NHAP BANG GIA:")
for i in range(len(sanpham)):
    for j in range(i+1, len(sanpham)):
            sanpham[i], sanpham[j] = sanpham[j], sanpham[i]
            gia[i], gia[j] = gia[j], gia[i]
    print(" Ten mat hang:", sanpham[i])
    print(" Gia ban hang:", gia[i])

print("NHAP HANG TON:")
while True:
    chon = input("  Ten mat hang : ")
    if chon == '':
        break
    else:
        if  chon in sanpham:
            index = sanpham.index(chon)
            so = int(input("  So luong ton kho: "))
            soluong.append(so)
        
if soluong:
    soton = [s * g for s, g in zip(soluong, gia)]
    sorted_soton = sorted(soton, reverse=True)

    print("\nTHONG KE HANG TON:")
    for i in range(len(sorted_soton)):
        
        print(sanpham[i],float(sorted_soton[i]))
        
