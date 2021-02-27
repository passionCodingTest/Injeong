import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
data = [i for i in range(n)]
slist = []
for _ in range(n):
    slist.append(list(map(int, input().split())))

canList = list(combinations(data, n//2))
min_value = 20001
cn = len(canList)

for i in range(0, cn//2):
    sum1 = 0
    sum2 = 0
    startList = list(combinations(canList[i], 2))
    linkList = list(combinations(canList[cn-i-1], 2))
    for i in range(0, len(startList)):
        n1 = startList[i][0]
        n2 = startList[i][1]
        sum1 += slist[n1][n2] + slist[n2][n1]
        link1 = linkList[i][0]
        link2 = linkList[i][1]
        sum2 += slist[link1][link2] + slist[link2][link1]
    min_value = min(min_value, abs(sum1-sum2))

print(min_value)
