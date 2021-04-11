from collections import deque

n,k = [int(i) for i in input().split()]
q = deque()
v = [False]*200001

ret = 10000001
q.append((n,0))

while q :
    cur = q.popleft()
    v[cur[0]] = True
    
    if cur[0] == k:
        if ret >= cur[1]:
            ret= cur[1]
        else:
            break
    
    if cur[1] > ret:
        break

    if cur[0]*2 <=200000 and not v[cur[0]*2] :
        q.appendleft((cur[0]*2, cur[1]))
    if cur[0]-1 >=0 and not v[cur[0]-1] :
        q.append((cur[0]-1,cur[1]+1))
    if cur[0]+1 <=200000 and not v[cur[0]+1] :
        q.append((cur[0]+1,cur[1]+1))


print(ret)