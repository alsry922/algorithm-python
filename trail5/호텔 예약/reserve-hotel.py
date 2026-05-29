n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
points = []

for i in range(n):
    si, ei = intervals[i]
    points.append((si, -1, i))
    points.append((ei, +1, i))

points.sort()
max_occupied = 0
occupied = set()
for x, v, i in points:
    if v == -1:
        occupied.add(i)
    else:
        occupied.remove(i)
    max_occupied = max(max_occupied, len(occupied))

print(max_occupied)