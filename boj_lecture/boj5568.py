import sys
from itertools import permutations

n = int(input())
k = int(input())
req = []
for i in range(n):
    req.append(int(input()))

pl = list(permutations(req, k))
result = []

for p in pl:
    temp = ''
    for a in p:
        temp += str(a)
    if temp not in result:
        result.append(temp)

print(len(result))