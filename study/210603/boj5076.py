def check(req):
    st = []
    for i in range(len(req)):
        if req[i] == '<':
            if req[i+1] == '/':
                left = i+2
            else:
                left = i+1
        if req[i] =='>':
            if req[i-1] =='/':
                continue

            right = i
            if st and st[-1] == req[left:right]:
                 st.pop()
            else:
                temp = req[left:right].split()
                st.append(temp[0])
    if st:
        print("illegal")
    else:
        print("legal")


while True:
    data = input()
    if data == '#':
        break

    check(data)
     
    