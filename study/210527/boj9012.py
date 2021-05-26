import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    temp = input()
    st = []
    check = True
    for t in temp:
        #공백인 경우 예외처리
        if t != '(' and t !=')':
            continue

        if t == '(':
            st.append(t)
        else:
            if st and st[-1] == '(':
                st.pop()
            else:
                check = False
                break

    if check and not st:
        print("YES")
    else:
        print("NO")