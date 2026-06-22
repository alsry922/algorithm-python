n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

# Please write your code here.
# 최소시간 후보값 x
# x이 줄어들수록 통과시킬 수 있는 물건의 양이 줄어듦
# 단조성 확인

def is_possible(x):
    cnt = 0
    for ele in arr:
        cnt += x // ele
    return cnt >= n

left, right = 1, n * 10 ** 9
answer = n * 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)