import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0] * n for i in range(n)]
direction = deque()
queue = deque()

#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(k):
    x, y = map(int,input().split())
    #사과 있음
    graph[x-1][y-1] = 1

l = int(input())

for i in range(l):
    x, y = input().split()
    direction.append((int(x),y))

#0 비어있는값
#-1 뱀 있는 깂
#1 사과

time = 0
dir = 3
graph[0][0] = -1
#꼬리 리스트
tailIdx = 0
#뱀의 기록을 담는 리스트
snake = [(0,0)] 
cx, cy = 0, 0


while True:

    time += 1

    nx = cx + dx[dir]
    ny = cy + dy[dir]

    print(cx, cy)
    snake.append((nx, ny))

    if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == -1:
        break

    

    if graph[nx][ny] == 0:
        lx = snake[tailIdx][0]
        ly = snake[tailIdx][1]
        graph[lx][ly] = 0
        tailIdx += 1

    graph[nx][ny] = -1
    
    #방향바꾸기
    if direction and time == direction[0][0]:
        sec, newdir = direction.popleft()
        #왼쪽으로
        if newdir == 'L': 
            dir += 1
        else:
            dir += 3
        dir %= 4

    cx = nx
    cy = ny

print(time)

