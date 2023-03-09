from math import factorial

def P(n, k):
    ans = factorial(n)/factorial(n-k)
    return ans

def C(n, k):
    ans = P(n, k)/factorial(k)
    return ans

n = int(input("inprt n "))
k = int(input("inprt k "))

print("P = ", P(n, k))
print("C = ", C(n, k))