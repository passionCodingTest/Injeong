import sys

input = sys.stdin.readline
n = int(input())
req = [0]
dp = [0] * (n+1)
for _ in range(n):
    req.append(int(input()))

if n == 1:
    print(req[1])
else:
    dp[1] = req[1]
    dp[2] = req[1] + req[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-3]+req[i-1]+req[i], dp[i-2]+req[i])

    print(max(dp))