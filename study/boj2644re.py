import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())

fam = [[]for _ in range(n+1)]
for i in range(m):
    x, y  = map(int, input().split())
    fam[x].append(y)
    fam[y].append(x)

visited = [0] * (n+1)

def dfs(v, cnt):
    if v == b:
        return cnt

    #fam[v]에 들어있는 node값. 즉, 연결되어있는 값만 탐색하도록 변경
    for i in fam[v]:
        if visited[i] == 0:
            if i == b:
                return cnt + 1
            
            visited[i] = 1
            dfs(i, cnt+1)

visited[a] = 1
result = dfs(a, 0)
print(result)
