m = int(input())
a, b = map(int, input().split())

# Please write your code here.
# 컴퓨터가 1 ~ M 까지의 수 중 하나를 선택
# 컴퓨터는 A이상 B 이하의 수 만을 선택
# 사람들은 항상 범우의 가운데 값을 고름
# 게임이 가장 빨리 끝날 때와 오래 끝날 때를 계산하는 프로그램을 작성하라.

# 완전 탐색이 가능한가?
# A이상 B이하의 수를 각각 하나씩 선택하여 이진 탐색을 진행하면?
#   B - A (P) = 100000 만큼 반복
#   m 범위를 이진 탐색 O(log m)
#       m은 최대 10 ^ 18 -> 18 * log10 ->
#   O(P log m) -> brute force 가능
MAX, MIN = float('inf'), float('-inf')
min_cnt, max_cnt = MAX, MIN
for target in range(a, b + 1):
    left, right = 1, m
    count = 0
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if mid == target:
            min_cnt = min(min_cnt, count)
            max_cnt = max(max_cnt, count)
            break
        if mid < target:
            left = mid + 1
        else:
            right = mid - 1

print(min_cnt, max_cnt)