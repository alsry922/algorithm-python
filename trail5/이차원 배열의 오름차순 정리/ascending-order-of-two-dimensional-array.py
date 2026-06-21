n = int(input())
k = int(input())

# Please write your code here.
# left = 1, right = N ** 2
# 후보값 x 가 10이라고 가정 x 이하의 수가 몇 개인가를 따졌을 때,
# 후보값 x가 증가할수록 x 이하의 수의 갯수도 단조 증가

# x 이하의 수가 몇 개인가
def count(x):
    # i * j <= x
    cnt = 0
    for i in range(1, n + 1):
        j = x // i
        cnt += min(j, n)
    return cnt
    

left, right = 1, n ** 2
while left <= right:
    mid = (left + right) // 2
    if count(mid) >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)