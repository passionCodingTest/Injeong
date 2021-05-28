import sys

input = sys.stdin.readline

n = int(input())
req = []
ans = 0
min_l = 1000
max_l = 1
max_idx = -1
max_h = -1
for i in range(n):
    #위치 높이
    l, h = map(int, input().split())
    if l < min_l:
        min_l = l
    if l > max_l:
        max_l = l
    if h > max_h:
        max_h = h
        max_idx = l

    req.append((l, h))

my_list = [0] * (max_l+1)

for l, h in req:
    my_list[l] = h

#왼쪽
temp = 0
for i in range(max_idx+1):
    if my_list[i] > temp:
        temp = my_list[i]
    ans += temp

#오른쪽
temp = 0
for i in range(max_l, max_idx, -1):
    if my_list[i] > temp:
        temp = my_list[i]
    ans += temp

print(ans)
