import sys
from collections import deque
input = sys.stdin.readline



dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]
t = int(input())

def bfs(l, i, j, tx, ty, visited):
    queue = deque()
    queue.append((i,j, 0))
    result = 99999999999
    while queue:
        x, y, count = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == tx and ny == ty:
                result = min(result, count+1)
            if nx >= 0 and nx < l and ny >= 0 and ny < l:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, count+1))
    return result
            
for i in range(t):
    l = int(input())
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())
    visited = [[False] * l for _ in range(l)]
    visited[x][y] = True
    if x == tx and x == ty:
        print(0)
        continue
    answer = bfs(l, x, y, tx, ty, visited)
    print(answer)
