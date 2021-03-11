import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
find = False

for i in range(n-1, 0, -1):
    if data[i-1] > data[i]:
        for j in range(n-1, 0, -1):
            if data[i-1] > data[j]:
                data[i-1], data[j] = data[j], data[i-1]
                data = data[:i]+sorted(data[i:], reverse=True)
                find = True
                break
            
        if find:
            print(*data)
            break

if not find:
    print(-1)