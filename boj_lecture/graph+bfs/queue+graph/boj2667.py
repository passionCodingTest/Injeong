import sys

input = sys.stdin.readline

n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    graph.append(list(input()))

def dfs(x, y, visited):
    global count
    count += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == '1' and visited[nx][ny] == False:
                dfs(nx, ny, visited)

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and visited[i][j] == False:
            count = 0
            dfs(i, j, visited)
            result.append(count)

print(len(result))
result.sort()
for i in result:
    print(i)