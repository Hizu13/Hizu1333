a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
A = []

A.append(a)
A.append(b)
A.append(c)
A = set(A)
A = sorted(A)

print("Xep tang dan:" , *A)
