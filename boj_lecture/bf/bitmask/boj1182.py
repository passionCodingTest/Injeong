import sys

input = sys.stdin.readline

n, s = map(int, input().split())
seq = list(map(int, input().split()))
count = 0

def recur(index, sum):
    global count
    if sum == s:
        count += 1

    for i in range(index+1, n):
        recur(i, sum + seq[i])

for i in range(n):
    recur(i, seq[i])

print(count)