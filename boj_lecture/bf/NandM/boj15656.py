import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def dfs():
    if len(answerList) == m:
        print(" ".join(map(str, answerList)))
        return
    
    for d in data:
        answerList.append(d)
        dfs()
        answerList.pop()


for d in data:
    answerList = []
    answerList.append(d)
    dfs()
