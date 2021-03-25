import sys

input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n)]
dp[0] = [req[0], -999999999]



for i in range(1, n):
    dp[i][0] = max(dp[i-1][0]+ req[i], req[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + req[i])

result = -999999999
for i in range(n):
    result = max(result, max(dp[i]))

print(result)