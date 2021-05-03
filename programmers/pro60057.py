def solution(s):
    answer = 10001
    if len(s) ==1:
        return 1
    for i in range(1, len(s)):
        count = 1
        result = ''
        target = s[0:i]
        j = i
        while j <= len(s):
            if target == s[j:j+i]:
                count += 1
            else:
                if count < 2:
                    result += target
                else:
                    result += str(count)
                    result += target
                target = s[j:j+i]
                count = 1
            if j+i > len(s):
                result += s[j:]
                break
            j = j+i
        answer = min(answer, len(result))
    return answer