def isFibonacci(N):
    if N == 0 or N == 1:
        return True
    a, b = 0, 1
    while True:
        c = a + b
        a = b
        b = c
        if c == N:
            return True
        elif c >= N:
            return False
n = int(input("N = "))
if (isFibonacci(n) == True):
        if(n%2 == 0):
             print("N la so fibonacci chan")
        else:
            print("N khong phai la so fibonacci chan")
else:
        print("N khong phai la so fibonacci chan")