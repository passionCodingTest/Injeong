import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = []
visited = [[False]*m for i in range(n)]

for i in range(n):
    graph.append(list(input()))


q = deque()
q.append((0, 0, 0))

visited[00][0] = True
check = False

while q:
    cur = q.popleft()
    cx, cy, count = cur[0], cur[1], cur[2]
    if cx == n-1 and cy == m-1:
        print(count + 1)
        break

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >=m:
            continue

        if not visited[nx][ny] and  graph[nx][ny] == '1':
            q.append((nx, ny, count + 1))
            visited[nx][ny] = True

    