import sys
import math

input = sys.stdin.readline

n = int(input())
ans = 0
while n > 0:
    temp = int(math.sqrt(n))
    n -= temp**2
    ans += 1

print(ans)