from sortedcontainers import SortedList
n, d = map(int, input().split())
points = [(-1, -1)] + [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
# y 좌표값을 기준으로 좌표 오름차순 정렬
points.sort(key=lambda x: x[1])
# x 좌표값만 오름차순 정렬
px = SortedList(x)
MAX = float('inf')
answer = MAX
j = 0

for i in range(1, n + 1):
    while j + 1 <= n and points[j + 1][1] - points[i][1] < d:
        px.remove(points[j + 1][0])
        j += 1

    xi = px.bisect_left(points[i][0])
    if xi < len(px):
        answer = min(answer, abs(points[i][0] - px[xi]))
    if xi > 0:
        ansswer = min(answer, abs(points[i][0] - px[xi - 1]))
    

print(-1 if answer == MAX else answer)