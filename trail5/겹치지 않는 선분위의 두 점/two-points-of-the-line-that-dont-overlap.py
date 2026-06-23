import bisect
n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]
segments.sort()
x1s = [x1 for x1, x2 in segments]
x2s = [x2 for x1, x2 in segments]

# Please write your code here.
# 후보값 d: 가장 가까운 두 점 거리의 최댓값
# 후보값 d를 가정했을 떄 조건을 만족하는가?
# 최소 거리가 d 이상이 되도록 N개의 점을 배치할 수 있는가?

def is_possible(d):
    cnt = 1
    last_pos = x1s[0]
    while cnt < n:
        lb = bisect.bisect_left(x2s, last_pos + d)
        if lb == m:
            return False
        last_pos = max(segments[lb][0], last_pos + d)
        cnt += 1
    return True

left, right = 0, 10 ** 18 + 1
answer = 0
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)