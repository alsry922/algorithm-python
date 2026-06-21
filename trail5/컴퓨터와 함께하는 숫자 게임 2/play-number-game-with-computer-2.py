import sys
m = int(input())
a, b = map(int, input().split())

# Please write your code here.
# 컴퓨터가 1 ~ 10^18의 수 중 A ~ B 까지의 수를 선택
# A ~ B 모든 선택을 시뮬레이션 했을 때, 가장 적은 정답 시도와 가장 많은 정답 시도를 출력
#   A~B 까지의 모든 수를 가지고 정답 시도 횟수를 구함
#   가장 많은 시도와 가장 적인 시도를 구해서 갱신

def get_cnt(x):
    left, right = 1, m
    cnt = 0
    while left <= right:
        cnt += 1
        mid = (left + right) // 2
        # print(left, mid, right)
        if x == mid:
            return cnt
        if x < mid:
            right = mid - 1
        else:
            left = mid + 1
    return cnt


MIN, MAX = -sys.maxsize, sys.maxsize
min_cnt, max_cnt = MAX, MIN
for x in range(a, b + 1):
    cnt = get_cnt(x)
    min_cnt = min(min_cnt, cnt)
    max_cnt = max(max_cnt, cnt)

print(min_cnt, max_cnt)