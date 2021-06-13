import sys

input = sys.stdin.readline

n = int(input())
st = []
graph = []
ans = 0

for i in range(n):
    graph.append(int(input()))
    while st and graph[st[-1]] > graph[i]:
        j = st.pop()
        width = i
        if st:
            width -= st[-1] + 1
        print(st)
        temp = width * graph[j]
        if ans < temp:
            ans = temp
    st.append(i)

while st:
    print(st)
    j = st.pop()
    width = n
    if st:
        width -= st[-1] + 1
    temp = width * graph[j]
    if ans < temp:
        ans = temp
print(ans)