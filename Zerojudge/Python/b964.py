i = int(input())
n = list(map(int, input().split(' ')))
n.sort()

maxiuma, minuma = max(n), min(n)

print(n, maxiuma, minuma, end='')