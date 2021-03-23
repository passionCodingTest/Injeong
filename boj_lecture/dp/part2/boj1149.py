import sys

input = sys.stdin.readline

n = int(input())
colors = []
check = [] * n
for _ in range(n):
    r, g, b = map(int, input().split())
    colors.append([r, g, b])

dp = colors

for i in range(1, n):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])


print(min(dp[n-1]))