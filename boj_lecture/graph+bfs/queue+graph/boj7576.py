import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())

graph = []
visited = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
queue = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] != -1:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
                elif graph[nx][ny] > graph[x][y] + 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))
bfs()
max_value = 0
for i in range(n):
    if 0 in graph[i]:
        max_value = 0
        break
    max_value = max(max_value, max(graph[i]))
print(max_value-1)
