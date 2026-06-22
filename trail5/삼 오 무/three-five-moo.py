import math
n = int(input())

# Please write your code here.
# 후보값 x가 작아질 수록 non-Moo의 갯수도 작아진다.
# 후보값 x가 조건을 만족하는가
#   non-Moo의 갯수(x - Moo 갯수) >= N이어야 함.

# x까지의 수에서 non-Moo의 갯수
def count(x):
    mul3_cnt = x // 3
    mul5_cnt = x // 5
    lcm_cnt = x // math.lcm(3, 5)
    return x - (mul3_cnt + mul5_cnt - lcm_cnt)

left, right = 1, 2 * 10 ** 9
answer = 2 * 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if count(mid) >= n:
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1

print(answer)