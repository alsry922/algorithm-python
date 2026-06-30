n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
segments.sort()
# 가장 가까운 두 점의 거리 d
# d의 최댓값을 출력하는 문제
# 0 <= d <= 10 ** 18 이기 때문에, 모든 d에 대해서 완전탐색은 불가능

# 이분 탐색으로 d의 범위를 좁혀가면서 답을 찾을 수 있나?
# d가 특정 값 이상이면 N개의 점을 배치할 수 없음.
# d가 특정 값 미만이면 N개의 점을 배치할 수 있음.
# 단조성 확인 -> 이분 탐색 가능

# 수도코드
# segmets.sort()
# 결정함수(d):
#   point_count = 0
#   last_pos = -1
#   for i in range(m):
#       start, end = segments[i]
#       last_pos = max(last_pos, start)
#       point_count += 1
#       cnt = (end - last_pos) // d
#       last_pos = last_pos + cnt * d
#       point_count += cnt
#   return point_count >= n

def is_possible(d):
    point_count = 0
    last_pos = -1
    for i in range(m):
        start, end = segments[i]
        last_pos = max(start, last_pos)
        point_count += 1
        cnt = (end - last_pos) // d
        last_pos = last_pos + cnt * d + d
        point_count += cnt
        
    return point_count >= n

left, right = 1, 10 ** 18
answer = 1
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)