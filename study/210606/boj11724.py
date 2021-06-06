import sys

def dfs(graph, cur, visited):
    for i in graph[cur]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)



input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
ans = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(n):
    if not visited[i]:
        visited[i] = True
        dfs(graph, i, visited)
        ans += 1

print(ans)