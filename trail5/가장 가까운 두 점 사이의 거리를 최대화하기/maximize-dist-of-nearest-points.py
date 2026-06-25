n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
segments.sort()
# Please write your code here.
# 후보값 d: 두 점사이의 최소 거리, 단 각 선분당 하나씩 점을 배치해야 함.
# 결정함수
#   d를 가정했을 때 각 선분당 하나씩 점을 배치할 수 있는가?
#   d가 커지면 배치하 수 있는 점의 갯수가 줄어듦
#   d가 작아지면 배치할 수 있는 점의 갯수가 커짐

def is_possible(d):
    last_pos = segments[0][0]
    cnt = 1
    for x1, x2 in segments[1:]:
        if last_pos + d > x2:
            return False
        last_pos = max(last_pos + d, x1)
    return True

# print(is_possible(5))

left, right = 0, 10 ** 9
answer = 0
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)