from sortedcontainers import SortedList
MAX_X = 1000000

n, d = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
# x, y = zip(*points)
# x, y = list(x), list(y)

# Please write your code here.
answer = MAX_X
points.sort(key=lambda x: x[1])
px = SortedList([x[0] for x in points])
# points = [(-1, -1)] + points
# y를 기준으로 좌표를 정렬한다.


j = 0
for i in range(n - 1):
    # i인덱스 좌표와, j인덱스 좌표의 y값 차이가 D 미만인 경우
    while j < n and points[j][1] - points[i][1] < d:
        # D 미만인 구간의 x좌표는 필요없으므로 px에서 제거한다.
        px.remove(points[j][0])
        # j를 증가시킨다.
        j += 1
    # y값 차이가 D 이상인 경우가 나오면 while문을 종료한다.
    xi = points[i][0]
    pos = px.bisect_left(xi)
    if pos < len(px):
        answer = min(answer, abs(px[pos] - xi))
    if pos > 0:
        answer = min(answer, abs(px[pos - 1] - xi))
        
print(-1 if answer == MAX_X else answer)
