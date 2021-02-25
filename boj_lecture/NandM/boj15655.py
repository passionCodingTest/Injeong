import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = list(combinations(data, m))

for ans in answer:
    print(" ".join(map(str, ans)))
