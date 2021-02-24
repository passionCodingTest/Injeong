import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
data = []

for i in range(1, n+1):
    data.append(i)

answer = list(permutations(data, m))

for d in answer:
    for i in range(len(d)):
        print(d[i], end=" ")
    print()

'''
answer_list = [0] * m
check_list = [False] * (n+1)


def dfs(i):
    if i == m:
        print(" ".join(map(str, answer_list)))
        return

    for x in range(1, n + 1):
        if check_list[x]:
            continue

        check_list[x] = True
        answer_list[i] = x
        dfs(i + 1)
        check_list[x] = False

dfs(0)
'''