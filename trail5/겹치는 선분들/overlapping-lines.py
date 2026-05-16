N, K = map(int, input().split())
M = []
dir = []

for _ in range(N):
    m, d = input().split()
    M.append(int(m))
    dir.append(d)

# Please write your code here.
segments = []
for i in range(N):
    dist = M[i]
    d = dir[i]

    if i == 0:
        x1 = 0
    else:
        x1 = segments[i - 1][1]

    if d == 'R':
        x2 = x1 + dist
    
    if d == 'L':
        x2 = x1 - dist

    segments.append((x1, x2))

for index, (x1, x2) in enumerate(segments):
    if x2 < x1:
        segments[index] = (x2, x1)

points = []
for x1, x2 in segments:
    points.append((x1, 1))
    points.append((x2, -1))

points.sort()
answer = 0
sum_val = 0
for i in range(len(points)):
    x, v = points[i]
    sum_val += v
    if sum_val >= K:
        answer += (points[i + 1][0] - points[i][0])

print(answer)

