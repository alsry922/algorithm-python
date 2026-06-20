n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

def is_possible(target):
    count = 0
    # 각 원소가 target으로 몇 번 나누어지는 지 확인
    for ele in arr:
        count += ele // target
    # print(target, count)
    return count >= m

left, right = 1, 100000
MIN = 0
answer = MIN
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)