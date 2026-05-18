n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
points = []
for index, (x1, x2) in enumerate(intervals):
    points.append((x1, +1, index))
    points.append((x2, -1, index))

points.sort()
seg = set()
start = points[0][0]
end = 0
answer = 0
# 새로운 선분이 시작되면 구간 합을 다시 계산
for x, v, index in points:
    # 시작점인 경우
    if v == 1:
        # 남아있는 선분이 없다면 새로운 구간 시작
        if not seg:
            # 새로운 구간 시작이니까 기존 구간의 길이를 저장 후 새로운 구간 시작
            start = x
        seg.add(index)
    else:
        end = x
        seg.remove(index)
        if not seg:
            answer += (end - start)
    # print(seg)

print(answer)
