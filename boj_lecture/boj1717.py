import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(target):
    if target == parent[target]:
        return target
    
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)



###시간초과 --> 유니온 파인드로 해결해야함
'''
group = [[i] for i in range(n+1)]

for i in range(m):
    c, a, b = map(int, input().split())
    #같은 집합인지 확인
    if c == 1:
        check = False
        for gl in group:
            if a in gl and b in gl:
                print("YES")
                check = True
                break
        if not check:
            print("NO")
    else:
        count = 0
        for i in range(len(group)):
            if a in group[i]:
                ai = i
                count += 1
            if b in group[i]:
                bi = i
                count += 1
            if count == 2:
                break
        if ai != bi:
            group[ai] = group[ai] + group[bi]
            del group[bi]
        print(group)
'''
            