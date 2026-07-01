n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))
MIN_NUM, MAX_NUM = 1, 10 ** 9
# Please write your code here.
# n명의 위치 x, 이동속도 v가 주어졌을 때, 모두가 도달할 수 있는 특정 위치까지 가는데 걸리는 최소 시간 출력
# 최소 시간을 출력해야함.
# 위치가 1 ~ 10 ** 9 이고, 속도도 1 ~ 10 ** 9
# 모든 시간에 대해 시뮬레이션하면 시간제한 초과 발생할 수 있음.

# 이분탐색으로 답이 될수 있는 시간의 범위를 줄여 나가는 것이 가능한가?
# 최소 시간이 특정 값 미만일 때, 모든 사람이 도달할 수 없는 곳이 있음.
# 최소 시간이 특정 값 이상일 때, 모든 사람이 도달할 수 있는 곳이 생김.
# 단조성 확인
# n에 대하여 순회하면서 이 값이 답이 될 수 있는지 확인하면
# 최종 시간복잡도는 O(N log 10^9) -> 약 300만번으로 시간복잡도가 만족됨.

# 결정함수(t)
# n을 순회하면서 시뮬레이션
# xi +- vi * t -> 갈 수 있는 범위(x1, x2) 구함
# 다음 위치의 사람이 갈 수 있는 범위도 구하면서
# (x1, x2)의 공통 범위를 좁혀나가고 공통 범위 안에 들어오지 못하는 사람이 생기면
# 해당 t 값은 답이 될 수 없음.

def is_possible(t):
    x1 = MIN_NUM - 1
    x2 = MAX_NUM + 1
    for xi, vi in zip(x, v):
        x1i, x2i = max(0, xi - vi * t), min(10 ** 9, xi + vi * t)
        x1, x2 = max(x1i, x1), min(x2i, x2)
        if x1 > x2:
            return False
    return True

# 모두 다른 곳에 산다는 조건이 없음.
# 모두 같은 곳에 살면 이동할 필요 없으니까, 시간은 0
# 최악의 경우는 2명이 정반대 살면서 이동속도가 1인 경우, 시간은 10 ** 9 - 1
left, right = 0, 10 ** 9
for _ in range(100):
    mid = (left + right) / 2
    if is_possible(mid):
        right = mid
    else:
        left = mid

print(f'{mid:.4f}')