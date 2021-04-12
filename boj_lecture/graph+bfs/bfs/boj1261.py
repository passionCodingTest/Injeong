import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
graph = []
visited = [[0]*n for _ in range(m)]
check = [[False]*n for _ in range(m)]

for i in range(m):
    graph.append(list(input()))

queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >=n:
            continue
        if graph[nx][ny] == '1':
            if check[nx][ny] == False:
                visited[nx][ny] = visited[x][y] + 1
                check[nx][ny] = True
                queue.append((nx, ny))
            elif visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
        else:
            if check[nx][ny] == False:
                check[nx][ny] = True
                visited[nx][ny] = visited[x][y]
                queue.append((nx, ny))
            elif visited[nx][ny] > visited[x][y]:
                visited[nx][ny] = visited[x][y]
                queue.append((nx, ny))


#print(visited)
print(visited[m-1][n-1])

