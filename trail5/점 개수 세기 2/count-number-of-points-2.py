from sortedcontainers import SortedSet
n, q = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]

def print_grid(grid):
    for row in grid:
        print(row)
    print()

xs = SortedSet()
ys = SortedSet()
psum = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]
for point in points:
    x, y = point
    xs.add(x)
    ys.add(y)

for x, y in points:
    xp = xs.bisect_left(x) + 1
    yp = ys.bisect_left(y) + 1    
    psum[xp][yp] = 1

# Please write your code here.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        psum[i][j] += (psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1])

for query in queries:
    x1, y1, x2, y2 = query
    x1i = xs.bisect_left(x1) + 1
    y1i = ys.bisect_left(y1) + 1
    x2i = xs.bisect_right(x2)
    y2i = ys.bisect_right(y2)
    print(psum[x2i][y2i] - psum[x2i][y1i - 1] - psum[x1i - 1][y2i] + psum[x1i - 1][y1i - 1])