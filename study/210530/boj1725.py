import sys

input = sys.stdin.readline

n = int(input())
st = []
ans = 0
graph = []
for i in range(n):
    graph.append(int(input()))
    while st and graph[st[-1]] > graph[i]:
        j = st.pop()
        width = i
        if st:
            width -= st[-1] + 1
        temp = graph[j] * width
        if temp > ans:
            ans = temp
    st.append(i)

while st:
    j = st.pop()
    width = n
    if st:
        width -= st[-1] + 1
    temp = graph[j] * width
    if temp > ans:
        ans = temp

print(ans)