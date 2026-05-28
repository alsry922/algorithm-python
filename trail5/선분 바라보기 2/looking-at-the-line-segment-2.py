from sortedcontainers import SortedSet
n = int(input())

points = []
for i in range(n):
    yi, x1i, x2i = map(int, input().split())
    points.append(( x1i, +1, i, yi ))
    points.append(( x2i, -1, i, yi ))

# Please write your code here.
points.sort()
segs = SortedSet()
visible = [False] * n
cnt = 0
for x, v, index, y in points:
    if v == 1:
        segs.add((y, index))
    
    else:
        segs.remove((y, index))
    
    if not segs:
        continue
    
    if not visible[segs[0][1]]:
        visible[segs[0][1]] = True
        cnt += 1

print(cnt)