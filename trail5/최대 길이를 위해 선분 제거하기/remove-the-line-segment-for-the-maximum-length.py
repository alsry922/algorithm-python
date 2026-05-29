from sortedcontainers import SortedSet
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
points = []
for i in range(n):
    x1, x2 = segments[i]
    points.append(( x1, +1, i ))
    points.append(( x2, -1, i ))

points.sort()
prev_x = None
total_length = 0
active = SortedSet()
exclusive_only = [0] * n
for x, v, i in points:
    if prev_x is not None and active:
        length = x - prev_x
        total_length += length
        if len(active) == 1:
            only = active[0]
            exclusive_only[only] += length
    
    if v == 1:
        active.add(i)
    else:
        active.remove(i)

    prev_x = x

print(total_length - min(exclusive_only))