import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.insert(0, 0)
dp = data

for i in range(2, n+1):
    lm = i // 2
    for j in range(0, lm + 1):
        dp[i] = min(dp[i], dp[j] + dp[i-j])

print(dp[n])