n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# 후보값 x = 분배할 정수
# x 가 줄어들 수록 각 수에서 분배할 수 있는 횟수가 많아짐
# 단조성 확인
def is_possible(x):
    count = 0
    for ele in arr:
        count += ele // x
    return count >= m

left, right = 1, 100000
answer = 0

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)