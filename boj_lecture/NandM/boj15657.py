import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def dfs(index):
    if len(answerList) == m:
        print(" ".join(map(str, answerList)))
        return
    
    i = index
    for d in data[index:]:
        answerList.append(d)
        dfs(i)
        i += 1
        answerList.pop()

i = 0
for d in data:
    answerList = []
    answerList.append(d)
    dfs(i)
    i += 1
