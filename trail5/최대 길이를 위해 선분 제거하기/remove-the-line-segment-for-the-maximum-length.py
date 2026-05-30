n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# 어떤 선분을 제거했을 때 줄어드는 총 길이 = 그 선분의 단독 커버 구간 길이
# 따라서 총 길이 손실을 최소화하기 위해서는 단독 커버 구간 길이가 짧은 선분을 제거하면 됨
# 정답 = 총 길이 - min(각 선분의 단독 커버 구간 길이)

points = []

for i in range(n):
    x1, x2 = segments[i]
    points.append((x1, +1, i))
    points.append((x2, -1, i))

points.sort()
segs = set()
total_length = 0
prev_x = None
exclusive_cover_length = [0] * n
for x, v, index in points:

    if prev_x is not None and segs:
        length = x - prev_x
        total_length += length
        # 시작점이 하나 있는 경우 -> 현재 위치까지 선분이 하나였던 경우
        # 지금 위치까지 단독 커버 구간임.
        if len(segs) == 1:
            ci = list(segs)[0]
            # 단독 커버 구간의 길이를 구함.
            exclusive_cover_length[ci] += length
    # 시작점이면 segs에 추가
    if v == 1:
        segs.add(index)
    # 끝점이면 제거
    else:
        segs.remove(index)
    
    # 총 길이 계산

    # 마지막 x위치 갱신
    prev_x = x
print(total_length - min(exclusive_cover_length))