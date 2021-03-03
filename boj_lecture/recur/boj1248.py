import sys
input = sys.stdin.readline


def check(count):
    sum = 0
    for i in range(count, -1, -1):
        sum += result[i]
        if sum > 0 and s[i][count] <= 0:
            return False
        elif sum == 0 and s[i][count] != 0:
            return False
        elif sum < 0 and s[i][count] >= 0:
            return False
    return True

def recur(count):
    if count == n:
        return True

    if s[count][count] == 0:
        result[count] = 0
        return recur(count + 1)

    for i in range(1, 11):
        result[count] = s[count][count] * i
        if check(count) and recur(count+1):
            return True
    return False


n = int(input())
arr = list(input())
s = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        temp = arr.pop(0)
        if temp == '+':
            s[i][j] = 1
        elif temp == '-':
            s[i][j] = -1

result = [0] * n
recur(0)
print(' '.join(map(str, result)))