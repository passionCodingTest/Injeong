import sys

input = sys.stdin.readline

n = int(input())
input_data = list(map(int, input().split()))
input_data.insert(0, 0)
dp = input_data


for i in range(1, n+1):
    temp = i // 2
    for j in range(1, temp+1):
        dp[i] = max(dp[i], input_data[j] +input_data[i-j])

print(dp[n])