import sys


def dfs(n, graph, index, count, visited):
    global result
    if count == 4:
        result = True
        return

    for i in graph[index]:
        if visited[i] == False:
            visited[i] = True
            dfs(n, graph, i, count + 1, visited)
            visited[i] = False


input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
result = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(n, graph, i, 0, visited)
    if result:
        break



if result:
    print(1)
else:
    print(0)
 




