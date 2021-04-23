import sys

input = sys.stdin.readline

n, l = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(n)]

def check(lst):
    i = 0
    stack = 1
    now = lst[i]
    while i < n-1:
        i+=1
        diff = now - lst[i]
        #차이가 1보다 많이 나면
        if diff > 1 or diff <-1:
            return False
        # 1차이나면
        elif diff == 1:
            #경사로가 지도를 넘어가면
            if i+l > n:
                return False
            for j in range(i+1, i+l):
                if now - lst[j] != 1:
                    return False
            stack = 1 - l
        elif diff == -1:
            if i-l < 0 or stack < l:
                return False
            stack = 1
        else:
            stack += 1

        now = lst[i]
    return True
            
cnt = 0

#한줄씩 체크
for row in arr:
    if check(row):
        cnt += 1

for y in range(n):
    for x in range(n):
        if x > y:
            arr[y][x], arr[x][y] = arr[x][y], arr[y][x]

for row in arr:
    if check(row):
        cnt+=1

print(cnt)