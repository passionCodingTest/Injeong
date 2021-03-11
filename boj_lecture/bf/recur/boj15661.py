import sys
input = sys.stdin.readline

n = int(input())
data = [i for i in range(n)]
slist = []
min_value = 20001
total = 0
rsum = [0] * n
csum = [0] * n
for _ in range(n):
    slist.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        rsum[i] += slist[i][j]
        csum[j] += slist[i][j]
        total += slist[i][j]

#짝수면
if n % 2 == 0:
    cn = n // 2
else:
    cn = n // 2 + 1


def recur(index, count, sum):
    global min_value
    if count > cn or index >= n:
        return

    if count > 0:
        min_value = min(min_value, abs(sum))
    recur(index + 1, count + 1, sum - rsum[index] - csum[index])
    recur(index + 1, count, sum)


recur(0, 0, total)
print(min_value)
