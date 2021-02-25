import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = list(permutations(data, m))

for ans in answer:
    print(" ".join(map(str, ans)))
