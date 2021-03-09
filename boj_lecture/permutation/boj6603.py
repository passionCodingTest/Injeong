import sys
from itertools import combinations

input = sys.stdin.readline
slist = [] 
while True:
    slist.append(list(map(int, input().split())))
    if slist[len(slist)-1][0] == 0:
        break

slist.pop()
combi = []

for i in range(len(slist)):
    slist[i].pop(0)
    combi.append(list(combinations(slist[i], 6)))

for cb in combi:
    for c in cb:
        print(*c)
    print()