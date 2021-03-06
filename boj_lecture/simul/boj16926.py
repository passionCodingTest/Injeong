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


'''
시간초과 때문에 queue를 이용해서 구현할것
sys.setrecursionlimit(10**6)



#남동북서
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

#y,x 현재좌표 d현재방향 l넣어줄값 c현재그룹
def dfs(y, x, d, l, c):
    cur = graph[y][x]
    graph[y][x] = l

    ny = y + dy[d]
    nx = x + dx[d]

    if(d==3 and (ny==c and nx==c)):
        return
    if(ny >= c and ny < n-c and nx>=c and nx< m-c and not(ny==c and nx ==c)):
        dfs(ny, nx, d, cur, c)
    elif d+1 <4: #서쪽으로 진행하는 중이 아니고 더 이상 진행할 수 없으면
        ny=y+dy[d+1]
        nx=x+dx[d+1]
        if d==3 and (ny==c and nx==c): return
        dfs(ny, nx, d+1, cur, c)

s = 0 #그룹의 수
if n < m:
    s = n // 2
else:
    s = m//2

while r>0:
    for i in range(s):
        dfs(i, i, 0, graph[i][i+1], i)
    r = r-1


for i in range(n):
    print(*graph[i])
'''