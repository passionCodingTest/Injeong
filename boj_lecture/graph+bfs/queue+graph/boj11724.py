import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
result = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(visited, index):
    for i in graph[index]:
        if visited[i] == False:
            visited[i] = True
            dfs(visited, i)
    return True


visited = [False] * (n+1)

for i in range(1, n+1):
    if visited[i] == False:
        visited[i] = True
        if dfs(visited, i):
            result += 1

print(result)