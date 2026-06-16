import sys
from sortedcontainers import SortedList
n, d = map(int, input().split())
points = [(-1, -1)] + [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)
# Please write your code here.
# 점들을 y를 기준으로 정렬
# i가 증가할 때 두 수의 차가 줄어들 기 때문에 j를 증가시켜 차가 D 이상이 되도록 하는 수를 찾아야 함.
# 단조성 확인으로 투 포인터 사용 가능

# 좌표에서 x값만 정렬한 배열 정의
# while 문을 순회하며 최대로 선택할 수 있는 j를 탐색
# i좌표와 j좌표의 x값을 bisect로 
points.sort(key=lambda x: x[1])
px = SortedList(x)
j = 0
MAX = sys.maxsize
answer = MAX
for i in range(1, n + 1):
    while j + 1 <= n and abs(points[i][1] - points[j + 1][1]) < d:
        px.remove(points[j + 1][0])
        j += 1

    xi = px.bisect_left(points[i][0])
    if xi < len(px):
        answer = min(answer, abs(px[xi] - points[i][0]))
    if xi > 1:
        answer = min(answer, abs(px[xi - 1] - points[i][0]))

print(-1 if answer == MAX else answer)

# from sortedcontainers import SortedList
# n, d = map(int, input().split())
# points = [(-1, -1)] + [tuple(map(int, input().split())) for _ in range(n)]
# x, y = zip(*points)
# x, y = list(x), list(y)

# # Please write your code here.
# # y 좌표값을 기준으로 좌표 오름차순 정렬
# points.sort(key=lambda x: x[1])
# # x 좌표값만 오름차순 정렬
# px = SortedList(x)
# MAX = float('inf')
# answer = MAX
# j = 0

# for i in range(1, n + 1):
#     while j + 1 <= n and points[j + 1][1] - points[i][1] < d:
#         px.remove(points[j + 1][0])
#         j += 1

#     xi = px.bisect_left(points[i][0])
#     if xi < len(px):
#         answer = min(answer, abs(points[i][0] - px[xi]))
#     if xi > 0:
#         answer = min(answer, abs(points[i][0] - px[xi - 1]))
    

# print(-1 if answer == MAX else answer)
