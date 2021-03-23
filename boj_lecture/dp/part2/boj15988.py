import sys

n = int(input())
req = []

for _ in range(n):
    req.append(int(input()))

max_value = max(req) + 1 
dp = [0] * max_value
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_value):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for i in req:
    print(dp[i])