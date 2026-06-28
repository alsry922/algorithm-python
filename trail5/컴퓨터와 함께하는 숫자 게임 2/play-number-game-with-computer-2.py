m = int(input())
a, b = map(int, input().split())

# Please write your code here.
# 이미 있는 배열(m) 안에서 범위를 반씩 줄이며  a ~ b의 값을 찾음.
# 이진탐색으로 a ~ b를 찾으면 됨.
# O((b - a) * log m) 으로 시간복잡도를 만족시킴

# 수도코드
# min_cnt, max_cnt = 10 ** 18, 1
# for target in range(a, b + 1):
#   count = binary_search(target)
#   min_cnt = min(min_cnt, count)
#   max_cnt = max(max_cnt, count)

# 이진 탐색 횟수를 반환
def binary_search(x):
    left, right = 1, m
    count = 0
    while left <= right:
        mid = (left + right) // 2
        count += 1
        if mid == x:
            return count
        if x < mid:
            right = mid - 1
        else:
            left = mid + 1

min_cnt, max_cnt = m, 1
for i in range(a, b + 1):
    count = binary_search(i)
    min_cnt = min(min_cnt, count)
    max_cnt = max(max_cnt, count)
print(min_cnt, max_cnt)