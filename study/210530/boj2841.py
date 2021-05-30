import sys

input = sys.stdin.readline
n, p = map(int, input().split())
st = [[] for i in range(7)]
ans = 0

for i in range(n):
    line, pnum = map(int, input().split())
    while st[line] and st[line][-1] > pnum:
        st[line].pop()
        ans += 1
    
    if not st[line]:
        st[line].append(pnum)
        ans += 1
    elif st[line][-1] < pnum:
        st[line].append(pnum)
        ans += 1
    
print(ans)