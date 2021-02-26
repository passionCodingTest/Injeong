import sys

input = sys.stdin.readline

n = int(input())
req = []
for _ in range(n):
    req.append(int(input()))


def recur(sum, data):
    global count
    if sum > data:
        return
    if sum == data:
        count += 1
    
    for i in range(1, 4):
        recur(sum + i, data)

for data in req:
    count = 0
    recur(0, data)
    print(count)