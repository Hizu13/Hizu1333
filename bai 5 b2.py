F = [None] * 1000
def Fibonanci(N):
    if N == 1 or N == 0:
        F[N] = 1
        return 1
    else:
        So = Fibonanci(N - 1) + Fibonanci(N - 2)
        F[N] = So
        return So
def isFibo(N):
    Fibonanci(10)
    for i in range(0,1000):
        if N == F[i]:
            return True
    return False

N = int(input("Nhap N = "))
print(isFibo(N))