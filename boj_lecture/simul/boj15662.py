#톱니바퀴
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [deque(input().strip()) for _ in range(n)]


m = int(input())
req = []

for i in range(m):
    num, direc = map(int, input().split())

    #첫번째 톱니바퀴 회전
    arr[num-1].rotate(direc)
    
    #왼쪽 확인
    cur = arr[num-1][6+direc]
    nx = num - 2
    ndir = -direc
    while nx >=0:
        if arr[nx][2] != cur:
            arr[nx].rotate(ndir)
        else:
            break
        cur = arr[nx][6+ndir]
        nx -= 1
        ndir = -ndir 

    #오른쪽 확인
    cur = arr[num-1][2+direc]
    nx = num
    ndir = -direc
    while nx < n:
        if arr[nx][6] != cur:
            arr[nx].rotate(ndir)
        else:
            break
        cur = arr[nx][2+ndir]
        nx += 1
        ndir = -ndir
  
result = 0
for i in range(n):
    if arr[i][0] == '1':
        result += 1

print(result)