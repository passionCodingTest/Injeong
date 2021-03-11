import sys

input = sys.stdin.readline

n = int(input())
data = [i for i in range(1, n+1)]

print(*data)
find = False

while(True):
    for i in range(n-1, 0, -1):
        find = False
        if data[i-1] < data[i]:
            for j in range(n-1, 0, -1):
                if data[i-1] < data[j]:
                    data[i-1], data[j] = data[j], data[i-1]
                    data = data[:i]+sorted(data[i:])
                    find = True
                    break
        if find:
            print(*data)
            break
    if not find:
        break


