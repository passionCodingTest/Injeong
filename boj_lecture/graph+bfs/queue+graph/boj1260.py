import sys

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()
def bfs():
    queue = []
    result = []
    queue.append(v)
    visited = [False] * (n+1)
    visited[v] = True
    while queue:
        target = queue.pop(0)
        result.append(target)
            
        for i in graph[target]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    print(*result)

def dfs(index, visited):
    global result
    for i in graph[index]:
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            dfs(i, visited)

visited = [False] * (n+1)
visited[v] = True
result = [v]
dfs(v, visited)
print(*result)
bfs()

