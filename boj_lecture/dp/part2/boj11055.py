import sys

input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))

dp = [x for x in req]
dp[0] = req[0]

for i in range(n):
    for j in range(i):
        if req[i] > req[j]:
            dp[i] = max(dp[i], dp[j] + req[i])

print(max(dp))
