n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
points = []
for x1, x2 in intervals:
    points.append((x1, 1))
    points.append((x2, -1))

points.sort()
sum_val = 0
max_val = 0
for point in points:
    x, v = point
    sum_val += v
    max_val = max(max_val, sum_val)

print(max_val)