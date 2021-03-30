import sys
sys.setrecursionlimit(10**6)
def dfs(index, group):
    visited[index] = group
    
    for i in graph[index]:
        if visited[i] == 0:
            if dfs(i, -group) is False:
                return False
        elif visited[i] == visited[index]:
            return False
    return True


input = sys.stdin.readline
n = int(input())

for i in range(n):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1)
    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = True

    for i in range(1, v+1):
        if visited[i] == 0:
            if dfs(i, 1) is False:
                ans = False
                break
    print('YES' if ans else 'NO')


        
