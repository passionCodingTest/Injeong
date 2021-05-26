import sys
input = sys.stdin.readline

#그리디, 분할정복 이용

l, w, h = map(int, input().split())

n = int(input())
dict = {}
for i in range(n):
    a, b = map(int, input().split())
    dict[a] = b

#이전에 사용한 큐브
before = 0
ans = 0

#큰 큐브부터 넣는걸로
for i in range(n-1, -1, -1):
    before <<= 3
    possible = (l >> i) * (w >> i) * (h >> i) - before
    newCube = min(dict[i], possible)

    before += newCube
    ans += newCube


if before == l*w*h:
    print(ans)
else:
    print(-1)