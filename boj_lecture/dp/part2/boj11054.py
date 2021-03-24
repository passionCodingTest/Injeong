import sys

input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))

inc = [1] * n
dec = [1] * n
result = [0] * n
for i in range(n):
    for j in range(i):
        if req[i] > req[j]:
            inc[i] = max(inc[i], inc[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if req[i] > req[j]:
            dec[i] = max(dec[i], dec[j] + 1)
    result[i]  = inc[i] + dec[i] - 1

print(max(result))