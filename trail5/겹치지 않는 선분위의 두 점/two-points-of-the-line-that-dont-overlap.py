n, m = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(m)]
segments.sort()
# Please write your code here.
# 후보값 d: 두 점 사이의 최소 거리
# d를 특정 값으로 가정했을 때 n개 이상의 점을 선분 위에 배치 가능한가?
# 최소 거리를 d로 가정했을 때 n개 이상의 점을 배치 가능하다면, d를 증가시켜볼 수 있음
# 반대라면 d를 감소시켜야 함.

def is_possible(d):
    last_pos = segments[0][0]
    cnt = 1
    for i in range(m):
        x1, x2 = segments[i]
        while last_pos + d <= x2:
            last_pos = max(x1, last_pos + d)
            cnt += 1

            if cnt >= n:
                break
    
    return cnt >= n

left, right = 0, 10 ** 18 // (n - 1)
answer = 0
while left <= right:
    mid = (left + right) // 2
    # print(left, mid, right)
    if is_possible(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)