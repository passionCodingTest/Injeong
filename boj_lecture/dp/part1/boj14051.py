import sys

input = sys.stdin.readline

n = int(input())
tlist = [0]
plist = [0]
dp = [0] * (n+1)
for _ in range(n):
    t, p = map(int, input().split())
    tlist.append(t)
    plist.append(p)

for i in range(1, n+1):
    if i + tlist[i] > n+1:
        continue
    j = i
    dp[i] = max(dp[i], plist[i])
    for j in range(i+tlist[i], n+1):
        if j + tlist[j] > n+1:
            continue
        dp[j] = max(dp[j], dp[i] + plist[j])

print(max(dp))