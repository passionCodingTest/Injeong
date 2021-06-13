import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * m for i in range(n)]
visited = [[False]*m for i in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 0
for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1]  = 1


def dfs(x, y, count):    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >=n or ny < 0 or ny >=m:
            continue
        if not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            count = dfs(nx, ny, count + 1)
    return count

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            result = dfs(i, j, 0)
            if result > ans:
                ans = result

print(ans)