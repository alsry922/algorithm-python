n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
points = []
for i, (x1, x2) in enumerate(intervals):
    points.append((x1, 1, i))
    points.append((x2, -1, i))

points.sort()
segment = set()
answer = 0
for s, v, index in points:
    if v == 1:
        if not segment:
            answer += 1
        segment.add(index)
    else:
        segment.remove(index)

print(answer)