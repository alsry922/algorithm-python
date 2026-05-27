from sortedcontainers import SortedSet
n = int(input())
points = []
for i in range(n):
    yi, x1i, x2i = map(int, input().split())
    points.append( (x1i, +1, i, yi) )
    points.append( (x2i, -1, i, yi) )
visible = [False] * n

points.sort()
# Please write your code here.
segs = SortedSet()
cnt = 0
for _, v, index, y in points:
    # 시작점인 경우
    if v == 1:
        segs.add((y, index))
    # 끝점인 경우
    else:
        segs.remove((y, index))

    if segs and not visible[segs[0][1]]:
        visible[segs[0][1]] = True
        cnt += 1

print(cnt)