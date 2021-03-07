import sys

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

min_value = 1e9


def recur(start, index, cost, visited, count):
    global min_value

    if min_value <= cost:
        return

    if count+1 == n:
        if graph[index][start] != 0:
            cost += graph[index][start]
            min_value = min(min_value, cost)
        return

    for j in range(n):
        #방문한적이 있으면
        if visited[j]:
            continue
        #연결안됨
        if graph[index][j] == 0:
            continue
        visited[j] = True
        recur(start, j, cost + graph[index][j], visited, count+1)
        visited[j] = False


for i in range(n):
    visited = [False] * n
    visited[i] = True
    recur(i, i, 0, visited, 0)

print(min_value)
