def kiem_tra_cac_canh(A, B, C):
    if A+B>C and A+C>B and B+C>A:
        return True
    return False

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
if kiem_tra_cac_canh(A, B, C):
    print("dung la tam giac")
else:
    print("khong la tam giac")    