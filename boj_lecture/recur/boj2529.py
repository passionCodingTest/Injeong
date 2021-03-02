import sys

input = sys.stdin.readline
n = int(input())
kdata = list(map(str, input().split()))
#print(kdata)

max_value = 0
min_value = 9999999999
def recur(seq, ans):
    global max_value, min_value
    if len(ans) == n + 1:
        #print(ans)
        min_value = min(min_value, int("".join(map(str,ans))))
        max_value = max(max_value, int("".join(map(str,ans))))
        return

    k = kdata[seq]
    target = ans.pop()
    ans.append(target)
    if k == '>':
        for i in range(0, target):
            if i in ans:
                continue
            ans.append(i)
            recur(seq + 1, ans)
            ans.pop()
    else:
        for i in range(target+1, 10):
            if i in ans:
                continue
            ans.append(i)
            recur(seq + 1, ans)
            ans.pop()
    


ans = []
for i in range(10):
    ans.append(i)
    recur(0, ans)
    ans.pop()

if len(str(max_value)) < n+1:
    print('0'+str(max_value))
else:
    print(max_value)
if len(str(min_value)) < n+1:
    print('0'+str(min_value))
else:
    print(min_value)