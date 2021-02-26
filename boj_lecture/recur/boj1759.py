import sys

input = sys.stdin.readline

#최소 한개의 모음
#최소 두개의 자음
#오름차순 정렬

l, c = map(int, input().split())
req = list(map(str, input().split()))
req.sort()
check = ['a', 'e', 'i', 'o', 'u']


def recur(index, answer_list):
    if len(answer_list) == l:
        count = 0
        for ch in answer_list:
            if ch in check:
                count += 1
        if count >= 1 and l-count >= 2:
            print("".join(map(str, answer_list)))

    i = index+1
    for r in req[index+1:]:
        answer_list.append(r)
        recur(i, answer_list)
        answer_list.pop()
        i += 1


i = 0
for r in req:
    answer_list = []
    answer_list.append(r)
    recur(i, answer_list)
    i += 1
