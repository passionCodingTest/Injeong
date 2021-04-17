import sys

input = sys.stdin.readline

def reverse_up_down():
    global arr
    arr = arr[::-1]

def reverse_left_right():
    global arr
    for i in range(n):
        arr[i] = arr[i][::-1]

def rotate_right_90():
    global n, m, arr
    n, m = m, n
    copy_arr = [list(row)[::-1] for row in zip(*arr)]
    arr = copy_arr

def rotate_left_90():
    global n, m, arr
    n, m = m, n
    copy_arr = [list(row) for row in list(zip(*arr))[::-1]]
    arr = copy_arr

def suffle1():
    global arr
    copy_arr = [[0]*m for _ in range(n)]
    halfN = n//2
    halfM = m//2

    for i in range(halfN):
        for j in range(halfM):
            copy_arr[i][halfM+j] = arr[i][j]

    for i in range(halfN):
        for j in range(halfM, m):
            copy_arr[halfN+i][j] = arr[i][j]

    for i in range(halfN, n):
        for j in range(halfM, m):
            copy_arr[i][j-halfM] = arr[i][j]

    for i in range(halfN, n):
        for j in range(halfM):
            copy_arr[i-halfN][j] = arr[i][j]

    for i in range(n):
        for j in range(m):
            arr[i][j] = copy_arr[i][j]

def suffle2():
    global arr
    copy_arr = [[0]*m for _ in range(n)]
    halfN = n//2
    halfM = m//2

    for i in range(halfN):
        for j in range(halfM):
            copy_arr[halfN+i][j] = arr[i][j]

    for i in range(halfN, n):
        for j in range(halfM):
            copy_arr[i][j+halfM] = arr[i][j]

    for i in range(halfN, n):
        for j in range(halfM, m):
            copy_arr[i-halfN][j] = arr[i][j]

    for i in range(halfN):
        for j in range(halfM, m):
            copy_arr[i][j-halfM] = arr[i][j]

    for i in range(n):
        for j in range(m):
            arr[i][j] = copy_arr[i][j]

n, m, r = map(int, input().split())
arr = [input().split() for _ in range(n)]

for oper in input().split():
    if oper == '1':
        reverse_up_down()
    elif oper == '2':
        reverse_left_right()
    elif oper == '3':
        rotate_right_90()
    elif oper == '4':
        rotate_left_90()
    elif oper == '5':
        suffle1()
    elif oper == '6':
        suffle2()

for e in arr:
    print(*e)
