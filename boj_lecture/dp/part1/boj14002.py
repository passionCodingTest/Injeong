import sys

input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
dp = [1 for _ in range(n)]
result = []
max_v = 0
for i in range(n):
    for j in range(i):
        if req[i] > req[j]:
            dp[i] = max(dp[i], dp[j]+1)

count = max(dp)
idx = dp.index(count)
while idx >= 0:
    if dp[idx] == count:
        result.append(req[idx])
        count -= 1
    idx -= 1

print(max(dp))
for num in result[::-1]:
    print(num, end=' ')
    
