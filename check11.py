import math
 
# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# Returns true if n is a Fibonacci Number, else false
def isFibonacci(n):
 
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
    
# A utility function to test above functions
n = int(input("N = "))
if (isFibonacci(n) == True):
        if(n%2 == 0):
             print("N la so fibonacci chan")
        else:
            print("N khong phai la so fibonacci chan")
else:
        print("N khong phai la so fibonacci chan")