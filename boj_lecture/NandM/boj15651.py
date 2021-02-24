import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def dfs(count):
    if count == m:
        print(" ".join(map(str, answer_list)))
        return

    for j in range(1, n+1):
        answer_list.append(j)
        dfs(count+1)
        answer_list.pop()


for i in range(1, n+1):
    answer_list = []
    answer_list.append(i)
    dfs(1)
