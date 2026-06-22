n = int(input())
k = int(input())

# Please write your code here.
# 결정함수
# x가 k번째 이상인가?
def is_possible(x):
    cnt = 0
    
    for i in range(1, n + 1):
        cnt += min(x // i, n)
    return cnt >= k

left, right = 1, n ** 2
answer = n ** 2
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1

print(answer)