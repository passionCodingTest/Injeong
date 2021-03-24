import sys

input = sys.stdin.readline

n = int(input())

tg = []

for _ in range(n):
    tg.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    for j in range(len(tg[i])):
        tg[i][j] += max(tg[i+1][j], tg[i+1][j+1])
print(tg[0][0])