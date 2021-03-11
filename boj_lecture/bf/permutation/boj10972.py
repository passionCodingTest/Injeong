import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
find = False

for i in range(n-1, 0, -1):
    if seq[i-1] < seq[i]:
        for j in range(n-1, 0, -1):
            if seq[i-1] < seq[j]:
                seq[i-1], seq[j] = seq[j], seq[i-1]
                seq = seq[:i]+sorted(seq[i:])
                find = True
                break
    
    if find:
        print(*seq)
        break
if not find:
    print(-1)


