import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
data = []

for i in range(1, n+1):
    data.append(i)

answer = list(combinations(data, m))

for ans in answer:
    print(" ".join(map(str, ans)))