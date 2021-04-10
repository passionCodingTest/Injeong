import sys
from collections import deque
input = sys.stdin.readline

#모두 복사해서 클립보드 저장
#클립모드 화면에 붙여넣기
#화면에 있는 이모티콘중 하나 삭제
visited = [[-1] * 1001 for _ in range(1001)]
n = int(input())
queue = deque()
queue.append((1, 0))
visited[1][0] = 0
while queue:
    count, clipboard = queue.popleft()

    if visited[count][count] == -1:
        visited[count][count] = visited[count][clipboard] + 1
        queue.append((count, count))
    if count+clipboard <= n and visited[count+clipboard][clipboard] == -1:
        visited[count+clipboard][clipboard] = visited[count][clipboard] + 1
        queue.append((count+clipboard, clipboard))
    if count -1 >= 0 and visited[count-1][clipboard] == -1:
        visited[count-1][clipboard] = visited[count][clipboard]+1
        queue.append((count-1, clipboard))
    
r = visited[n][1]
for i in range(1, n):
    if visited[n][i] != -1:
        r = min(r, visited[n][i])
print(r)
