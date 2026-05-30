n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
points = []

# Please write your code here.
for i in range(n):
    si, ei = intervals[i]
    points.append((si - 1, +1, i))
    points.append((ei, -1, i))
points.sort()
max_occupied = 0
occupied = set()
for x, v, index in points:
    if v == 1:
        occupied.add(index)
        max_occupied = max(max_occupied, len(occupied))
    else:
        occupied.remove(index)

print(max_occupied)