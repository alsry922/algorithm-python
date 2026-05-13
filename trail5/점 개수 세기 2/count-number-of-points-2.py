from sortedcontainers import SortedSet
n, q = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]
def print_grid(grid):
    for row in grid:
        print(row)
    print('==========')
# Please write your code here.
xs = SortedSet()
ys = SortedSet()
psum = [
    [0] * (n + 1) for _ in range(n + 1)
]
for x, y in points:
    xs.add(x)
    ys.add(y)

for x, y in points:
    xi = xs.bisect_left(x) + 1
    yi = ys.bisect_left(y) + 1
    psum[xi][yi] += 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        psum[i][j] += (psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1])

for query in queries:
    x1, y1, x2, y2 = query
    lx = xs.bisect_left(x1) + 1
    rx = xs.bisect_right(x2)
    ly = ys.bisect_left(y1) + 1
    ry = ys.bisect_right(y2)
    
    print(psum[rx][ry] - psum[rx][ly - 1] - psum[lx - 1][ry] + psum[lx - 1][ly - 1])
