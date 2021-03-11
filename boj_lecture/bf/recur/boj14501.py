import sys

input = sys.stdin.readline

days = int(input())
req = []
req.append(0)
for i in range(days):
    req.append(list(map(int, input().split())))

#print(req)
max_value = 0


def recur(index, sum):
    global max_value
    if index > days:
        max_value = max(max_value, sum)
        return

    for i in range(index, days+1):
        t = req[i][0]
        p = req[i][1]
        if i + t > days + 1:
            max_value = max(max_value, sum)
            continue
        recur(i+t, sum + p)


for i in range(1, days+1):
    sum = 0
    t = req[i][0]
    p = req[i][1]
    if i + t > days + 1:
        continue
    recur(i + t, sum + p)

print(max_value)
