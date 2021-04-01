import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
graph = []

for _ in range(n):
    graph.append(list(input()))

def bfs(visited):
    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '1' and visited[x][y] + 1 < visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
visited = [[999999] * m for _ in range(n)]

visited[0][0] = 1
bfs(visited)
print(visited[n-1][m-1])



