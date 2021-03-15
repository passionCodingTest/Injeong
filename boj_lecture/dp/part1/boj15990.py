import sys

input = sys.stdin.readline

t = int(input())

dp = [[0] * 4 for _ in range(100001)]

dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 100001):
    for j in range(1, 4):
        dp[i][j] = (dp[i-j][1] + dp[i-j][2] + dp[i-j][3] - dp[i-j][j]) % 1000000009


for _ in range(t):
    id = int(input())
    result = (dp[id][1] + dp[id][2] + dp[id][3])  % 1000000009
    print(result)
