import sys

input = sys.stdin.readline

n = int(input())
req = input()
ls = []
op = ['+', '*', '-', '/']
st = []

for i in range(n):
    ls.append(int(input())) 

for s in req:
    if s in op:
        num1 = st.pop()
        num2 = st.pop()

        if s == '+':
            st.append(num2+num1)
        elif s == '-':
            st.append(num2-num1)
        elif s == '/':
            st.append(num2/num1)
        elif s == '*':
            st.append(num2*num1)
    else:
        if 'A' <= s <= 'Z':
            st.append(ls[ord(s)-ord('A')])
        else:
            st.append(s)

print("%.2f" %st[0])
