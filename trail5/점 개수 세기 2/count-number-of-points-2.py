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
for x, y in points:
    xs.add(x)
    ys.add(y)


grid = [
    [0 for _ in range(len(ys))]
    for _ in range(len(xs))
]

for x, y in points:
    xi = xs.bisect_left(x)
    yi = ys.bisect_left(y)
    grid[xi][yi] += 1

prefix_sum = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + \
                            prefix_sum[i-1][j] - \
                            prefix_sum[i-1][j-1] + \
                            grid[i-1][j-1]

for query in queries:
    x1, y1, x2, y2 = query
    xi1 = xs.bisect_left(x1) + 1
    yi1 = ys.bisect_left(y1) + 1
    xi2 = xs.bisect_right(x2)
    yi2 = ys.bisect_right(y2)

    print(prefix_sum[xi2][yi2] - prefix_sum[xi1 - 1][yi2] - prefix_sum[xi2][yi1 - 1] + \
        prefix_sum[xi1 - 1][yi1 - 1])
