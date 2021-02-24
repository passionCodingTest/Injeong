import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
data = []

for i in range(1, n+1):
    data.append(i)

answer = list(combinations(data, m))

for ans in answer:
    print(" ".join(map(str, ans)))

'''
answer_list = [0] * m
def dfs(index, selected):
    if selected == m:
        print(" ".join(map(str, ans)))
        return
    
    if index > n:
        return
    answer_list[selected] = index
    dfs(index + 1, selected + 1)
    answer_list[selected] = 0
    dfs(index + 1, selected)

dfs(1, 0)
'''