import sys

input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
dp = req

for i in range(1, n):
    if dp[i-1] >= req[i-1]:
        dp[i] = max(dp[i], dp[i-1] + req[i])

print(max(dp))

