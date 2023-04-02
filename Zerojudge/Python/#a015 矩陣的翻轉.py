'''
row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(input())
matrix = ' '.join(matrix)
matrix = matrix.split(' ')
for i in range(len(matrix)):
    for n in range(col):
        while(i%col!=0):
            print(i)
'''

import sys
mat = [[0] * 100 for i in range(100) ]   #宣告二維矩陣
for line in sys.stdin:
    m, n = line.split()
    m = int(m)
    n = int(n)
    for i in range(m):  #輸入陣列
        list = sys.stdin.readline().split()
        for j in range(n):
            mat[i][j] = list[j]
    for i in range(n):  #輸出順序改變就會達成轉置矩陣
        for j in range(m):
            print(mat[j][i]," ",sep="",end="")
        print()