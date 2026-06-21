import math
n = int(input())

# Please write your code here.
# 3, 5의 배수는 숫자 대신 Moo로 적는다.
# 1 ~ N 까지의 숫자 중 N 번째로 적히는 숫자를 구하라.
# 후보값 x를 증가시킬 수록 non-Moo의 갯수도 증가한다. -> 단조성
#   f(x) >= N 이 되는 가장 작은 값

# 후보값(target)의 범위를 절반씩 줄여가며,
# [1, target] 까지 범위에서 non-Moo의 갯수를 구한다.
def get_non_moo_cnt(target):
    mul3_cnt = target // 3
    mul5_cnt = target // 5
    lcm_cnt = target // math.lcm(3, 5)
    return target - (mul3_cnt + mul5_cnt - lcm_cnt)

# "답이 가질 수 있는 최솟값과 최댓값이 얼마야?" 항상 확인 필요
# N의 값이 10^9 이므로 right의 훨씬 더 커야한다.
left, right = 1, 2 * 10 ** 9
answer = 10 ** 10
while left <= right:
    mid = (left + right) // 2
    cnt = get_non_moo_cnt(mid)
    # print(left, right, cnt)
    if cnt >= n:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)