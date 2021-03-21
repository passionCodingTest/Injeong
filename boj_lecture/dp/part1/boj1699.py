import sys
from math import sqrt 
input = sys.stdin.readline
n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = i

for i in range(2, n+1):
    for j in range(1, int(i ** 0.5)+ 1):
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(dp[n])


'''
시간초과 발생시
min함수보단 if함수를 사용
j**2보단 j*j를 사용
'''