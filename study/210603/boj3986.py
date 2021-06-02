import sys

input = sys.stdin.readline

n = int(input())

ans = 0

for i in range(n):
    word = input()
    st = []
    for j in word:
        if st and st[-1] == j:
            st.pop()
        else:
            st.append(j)
    st.pop()
    if not st:
        ans += 1

print(ans)