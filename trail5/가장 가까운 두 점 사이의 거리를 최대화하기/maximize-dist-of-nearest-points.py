n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
segments.sort()
x1s = [x1 for x1, x2 in segments]
x2s = [x2 for x1, x2 in segments]
# Please write your code here.

# 후보값 d: 가장 가까운 두 점 사이의 거리
# n개 이상의 점을 d 이상의 거리로 배치할 수 있는가?
# 특정 d 값을 기준으로 n 개 이상 배치가 가능하다면 d 값을 늘려볼 수 있음.
# 특정 d 값을 기준으로 n 개 이상 배치가 불가능하다면 d 값을 낮춰야 함.

def is_possible(d):
    last_pos = x1s[0]
    cnt = 1
    for i in range(1, n):
        x1, x2 = segments[i]
        # x2가 마지막 점 + d 이상 거리보다 크다면 배치 가능
        if x2 >= last_pos + d:
            last_pos = max(x1, last_pos + d)
            cnt += 1
    return cnt >= n
# left: 완전히 선분히 겹치는 경우가 없으므로 1로 해도 무방하지만 0으로 설정
# right: 엄밀히 따지면 10 ** 9 // n 이 최대가 될 것 같은데 정확히 확신이 안서서 안전하게 10 ** 9로 설정
#   시간복잡도에 문제가 없으니까 괜찮음
left, right = 0, 10 ** 9
answer = 0
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)