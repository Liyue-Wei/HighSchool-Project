i = int(input())
def fibonacci(n):
    table = []
    def fib_table(n):
        if(n<=2):
            return 2
        table[n] = fib_table(n-1) + fib_table(n-2)
        return table[n]
    return fib_table[n]
'''
def fibonacci(n):
    if(n<=2):
        return 2
    return fibonacci(n-1) + fibonacci(n-2)
'''
while(i>0):
    n = int(input())
    print(fibonacci(n))
    i-=1