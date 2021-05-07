import sys

input = sys.stdin.readline

t = int(input())

for p in range(t):
    n = int(input())
    graph = [0] * (n+1)

    for i in range(n-1):
        a, b = map(int, input().split())
        graph[b] = a
    
    n1, n2 = map(int, input().split())
    n1p = [n1]
    n2p = [n2]
    while n1 != 0 or n2 != 0:
        if n1 != 0:
            n1p.append(graph[n1])
        if n2 != 0:
            n2p.append(graph[n2])
        n1 = graph[n1]
        n2 = graph[n2]
    if len(n1p) < len(n2p):
        for nt in n1p:
            if nt in n2p:
                print(nt)
                break
    else:
        for nt in n2p:
            if nt in n1p:
                print(nt)
                break



    



