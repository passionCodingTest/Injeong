import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque()
queue.append((n, 0))
visited = set()
visited.add(n)
while queue:
    location, count = queue.popleft()
    if location == k:
        print(count)
        break
    if location - 1 >=0 and location - 1 <= 100000 and location -1 not in visited:
        visited.add(location-1)
        queue.append((location - 1, count + 1))
    if location + 1 >=0 and location + 1 <= 100000 and location + 1 not in visited:
        visited.add(location+1)
        queue.append((location + 1, count + 1))
    if location * 2 >=0 and location * 2 <= 100000 and location * 2 not in visited:
        visited.add(location*2)
        queue.append((location * 2, count + 1))
