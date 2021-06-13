import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
req1, req2 = map(int, input().split())
m = int(input())
graph = [[] for i in range(n)]
visited = [False] * n
q = deque()
check = False

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

req1 -= 1
req2 -= 1


#bfs시작
q.append((req1,0))
visited[req1] = True

while q:
    cur = q.popleft()
    curNum = cur[0]
    curCount = cur[1]
    
    if curNum == req2:
        print(curCount)
        check = True
        break

    for i in graph[curNum]:
        if not visited[i]:
            q.append((i, curCount+1))
            visited[i] = True

if not check:
    print(-1)