import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(input().split())

def rotate(y, x, height, width):
    global graph
    q = deque()

    for i in range(x, x+width):
        q.append(graph[y][i])
    
    for i in range(y+1, y+height):
        q.append(graph[i][x+width-1])
    
    for i in range(x+width-2, x, -1):
        q.append(graph[y+height-1][i])
    
    for i in range(y+height-1, y, -1):
        q.append(graph[i][x])

    q.rotate(-r)
    #rotate 음수면 왼쪽으로 회전, 양수면 오른쪽으로 회전

    for i in range(x, x+width):
        graph[y][i] = q.popleft()
    
    for i in range(y+1, y+height):
        graph[i][x+width-1] = q.popleft()
    
    for i in range(x+width-2, x, -1):
        graph[y+height-1][i] = q.popleft()
    
    for i in range(y+height-1, y, -1):
        graph[i][x] = q.popleft()

height = n
width = m
y, x = 0, 0

while True:
    if height == 0 or width == 0: break

    rotate(y, x, height, width)
    y += 1
    x += 1
    height -= 2
    width -= 2

for i in range(n):
    for j in range(m):
        print(graph[i][j], end = ' ')
    print()
