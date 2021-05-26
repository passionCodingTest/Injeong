import sys

input = sys.stdin.readline
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
n = int(input())
board = [ [0] * 101 for i in range(101)]
for i in range(n):
    curve_size = 0
    curve = [0] * 1024
   
    x, y, d, g = map(int, input().split())
    
    curve[curve_size] = d
    curve_size += 1
    board[y][x] = 1

    for j in range(g):
        #역순으로 돌면서 커브를 90도씩 회전
        for k in range(curve_size-1, -1, -1):
            curve[curve_size] = (curve[k]+1) % 4
            curve_size += 1
    
    for j in range(curve_size):
        y += dy[curve[j]]
        x += dx[curve[j]] 
        if y < 0 or y >= 101 or x < 0 or x >= 101:
            continue
        board[y][x] = 1
    
ret = 0
for y in range(100):
    for x in range(100):
        if board[y][x] and board[y+1][x] and board[y][x+1] and board[y+1][x+1]:
            ret += 1


print(ret)



