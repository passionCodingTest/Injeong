import sys

input = sys.stdin.readline

req = input()
ans = ''
st = []

for i in req:
    if i.isalpha():
        ans += i
    else:
        if i == '(':
            st.append(i)
        elif i == '*' or i == '/':
            while st and (st[-1] == '*' or st[-1] =='/'):
                ans += st.pop()
            st.append(i)
        elif i == '+' or i == '-':
            while st and st[-1] != '(':
                ans += st.pop()
            st.append(i)
        elif i == ')':
            while st and st[-1] != '(':
                ans += st.pop()
            st.pop()    

while st:
    ans += st.pop()    
print(ans)