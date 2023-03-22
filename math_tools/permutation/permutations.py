'''
    說明:
    P_n取k = n!/(n-k)!
    U_n取k = n**k
    C_n取k = P_n取k/k!
    H_n取k = C_n+m-1取k
'''

from math import factorial
import os

def P(n, k):
    ans = factorial(n)/factorial(n-k)
    return ans
    
def U(n, k):
    ans = n**k
    return ans

def C(n, k):
    ans = P(n, k)/factorial(k)
    return ans

def H(n, k):
    ans = C(n+k-1, k)
    return ans

def fac(n):
    ans = factorial(n)
    return ans

n = int(input())
k = int(input())

if (n-k<0):
    print("False")

print(P(n, k))
print(C(n, k))
print(U(n, k))
print(H(n, k))
print(fac(n))

os.system("pause")