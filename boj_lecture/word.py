data = ["1 ROOTA 0", "2 AA 1", "3 ZZZ 1", "4 AABAA 1", '5 AAAAA 1', '6 AAAA 1', "7 BAAAAAAA 1", "8 BBAA 1", "9 CAA 1", "10 ROOTB 0", "11 AA 10"]
#data = ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]
#word = "BROWN" 
#word = "SALLY"

word = "AA"
n = len(data) + 1
wn = len(word)
datalist = [0] * n
parentList = [0] * n
treeList = [0] * n
leaf = []
answerList = []

for da in data:
    num, name, pa = da.split()
    num = int(num)
    pa = int(pa)
    datalist[num] = name
    parentList[num] = pa
    if pa > 0:
        treeList[num] = treeList[pa] + '/' + name
    else:
        treeList[num] = name

    
#리프 노드만 담음
for i in range(1, n):
    if i not in parentList:
        leaf.append(i)

#최종 결과 리스트
resultList = []
tempResult = []

#검색
for i in leaf:
    tempName = datalist[i]
    count = 0
    j = 0
    location = 0
    #이름이 아예 같은 경우는 미리 넣어줌
    if word == tempName:
        resultList.append(i)
        continue
    while True:
        if j >= len(tempName):
            break
        if word == tempName[j:j+wn]:
            count += 1
            location = j
            j = j+wn
        else:
            j +=1
    if count > 0:
        tempResult.append((i, count, location))

tempResult.sort(key=lambda x:(-x[1], x[2],x[0]))


if tempResult:
    for temp in tempResult:
       resultList.append(temp[0])

if not resultList:
    answer = "Your search for "+word+" didn't return any results"
    answerList.append(answer)
else:
    for i in resultList:
        answerList.append(treeList[i])

print(answerList)
