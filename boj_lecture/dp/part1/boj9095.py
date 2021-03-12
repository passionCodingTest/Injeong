import sys

input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))


dp = [0, 1, 2, 4]

for i in range(4, max(data)+1):
    dp.append(dp[i-1] + dp[i-2] +dp[i-3])

for d in data:
    print(dp[d])
