import sys

input = sys.stdin.readline
n = int(input())
req = []
for i in range(n):
    #나이 이름
    age, name = input().split()
    req.append((int(age), name, i))

req.sort(key = lambda x : (x[0], x[2]))
for re in req:
    print(re[0],re[1])