import sys


input = sys.stdin.readline
n = int(input())
data = [i for i in range(n)]
seq = list(map(int, input().split()))
find = False

def cal(data):
    sum = 0 
    for i in range(n-1):
        sum += abs(seq[data[i]] - seq[data[i+1]])
    return sum

max_value = cal(data)

while(True):
    for i in range(n-1, 0, -1):
        find = False
        if data[i-1] < data[i]:
            for j in range(n-1, 0, -1):
                if data[i-1] < data[j]:
                    data[i-1], data[j] = data[j], data[i-1]
                    data = data[:i] + sorted(data[i:])
                    find = True
                    break

            if find:
                max_value = max(max_value, cal(data))
                break
    if not find:
        break


print(max_value)
