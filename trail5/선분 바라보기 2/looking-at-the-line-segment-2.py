import heapq
n = int(input())

points = []
for i in range(n):
    yi, x1i, x2i = map(int, input().split())
    points.append(( x1i, +1, i, yi ))
    points.append(( x2i, -1, i, yi ))

# Please write your code here.
points.sort()
segs = []
deleted = set()
visible = [False] * n
cnt = 0
for x, v, index, y in points:
    # 시작점이면 추가
    if v == 1:
        heapq.heappush(segs, (y, index))
    else:
        deleted.add((y, index))
    
    if not segs:
        continue
    
    while segs and segs[0] in deleted:
        heapq.heappop(segs)
    
    if segs and not visible[segs[0][1]]:
        visible[segs[0][1]] = True
        cnt += 1

print(cnt)