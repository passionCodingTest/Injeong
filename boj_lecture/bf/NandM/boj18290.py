n, m, k = map(int, input().split())
answer_list = [list(map(int, input().split())) for _ in range(n)]
check_list = [[False] * m for _ in range(n)]
ans = -2147483647
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(px, py, cnt, sum):
    global ans

    if cnt == k:
        ans = max(ans, sum)
        return

    for x in range(px, n):
        for y in range(py if x == px else 0, m):
            if check_list[x][y]:
                continue

            ok = True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if check_list[nx][ny]:
                        ok = False

            if ok:
                check_list[x][y] = True
                dfs(x, y, cnt + 1, sum + answer_list[x][y])
                check_list[x][y] = False


dfs(0, 0, 0, 0)
print(ans)
