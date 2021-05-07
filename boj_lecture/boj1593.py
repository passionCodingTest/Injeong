import sys

input = sys.stdin.readline
#w의 길이, s의길이
g, sn = map(int, input().split())
w = input().strip()
s = input().strip()

wl = [0] * 52
sl = [0] * 52

for i in range(g):
    if 'a' <= w[i] <= 'z':
        wl[ord(w[i]) - ord('a')] += 1
    else:
        wl[ord(w[i]) - ord('A')+26] += 1

start, length, count = 0, 0, 0

for i in range(sn):
    if 'a' <= s[i] <= 'z':
        sl[ord(s[i]) - ord('a')] += 1
    else:
        sl[ord(s[i]) - ord('A') + 26] += 1
    
    length += 1

    if length == g:
        if wl == sl:
            count += 1
        if 'a' <= s[start] <= 'z':
            sl[ord(s[start]) - ord('a')] -= 1
        else:
            sl[ord(s[start]) - ord('A') + 26] -= 1
        start += 1
        length -= 1

print(count)



##순열을 사용해서 메모리초과 TT
'''
from itertools import permutations

input = sys.stdin.readline
ans = 0
#w의 길이, s의길이
g, sn = map(int, input().split())

w = list(input().strip())
s = list(input().strip())

#w의 경우의 수
wc = list(permutations(w, g))

for wl in wc:
    j = 0
    while j < sn:
        check = True
        for i in range(g):
            if j >= sn:
                check = False
                break
            if wl[i] != s[j]:
                check = False
                break
            j += 1
        if check:
            ans += 1
        else:
            j += 1
print(ans)
'''
