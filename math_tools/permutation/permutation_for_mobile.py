from math import factorial
import os

def P(n, k):
    ans = factorial(n)/factorial(n-k)
    return ans

def C(n, k):
    ans = P(n, k)/factorial(k)
    return ans

n = int(input("input n "))
k = int(input("input k "))

print("P = ", P(n, k))
print("C = ", C(n, k))

os.system("pause")