'''
def isprime(n):
    if n in [2, 3, 5]:
        return True
    if n < 2 or (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0:
        return False
    if n < 49:
        return True
    if (n %  7) == 0 or (n % 11) == 0 or (n % 13) == 0 or (n % 17) == 0 or \
       (n % 19) == 0 or (n % 23) == 0 or (n % 29) == 0 or (n % 31) == 0 or \
       (n % 37) == 0 or (n % 41) == 0 or (n % 43) == 0 or (n % 47) == 0:
        return False
    if n < 2809:
        return True
    if n < 31417:
        return pow(2, n, n) == 2 and n not in [7957, 8321, 13747, 18721, 19951, 23377]
'''
def isprime(n):
    if(n%6==1 or n%6==5):
        return True
    else:
        return False
    
while(True):
    try:
        i = int(input())
        if(isprime(i)):
            print("質數")
        else:
            print("非質數")
    except:
        break

'''
from sympy import *
while(True):
    try:
        i = int(input())
        if(isprime(i)):
            print("質數")
        else:
            print("非質數")
    except:
        break
'''