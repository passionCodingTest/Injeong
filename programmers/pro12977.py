from itertools import combinations
def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    temp = list(combinations(nums, 3))
    for arr in temp:
        s_v = sum(arr)
        if isPrime(s_v):
            answer += 1
    return answer
