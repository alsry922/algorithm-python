import bisect

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
xs = [x for x, y in points]
ys = [y for x, y in points]
MAX_X = max(xs)
MAX_Y = max(ys)
answer = float('inf')
# 2차원 grid에 좌표 위치 저장
grid = [
    [0 for _ in range(MAX_Y + 1)]
    for _ in range(MAX_X + 1)
]
gsum = [
    [0] * (MAX_Y + 1) for _ in range(MAX_X + 1)
]        

for x, y in points:
    grid[x][y] += 1

def print_grid(grid):
    for row in grid:
        print(row)
    print('================')
# print_grid(grid)

for i in range(1, MAX_X + 1):
    for j in range(1, MAX_Y + 1):
        gsum[i][j] = gsum[i-1][j] + gsum[i][j-1] - gsum[i-1][j-1] + grid[i][j]

# print_grid(gsum)

for x in xs:
    for y in ys:
        # 2사분면
        quad2 = gsum[x][y]
        # 1사분면
        quad1 = gsum[x][MAX_Y] - quad2
        # y열 미만에서 2사분면 빼면 3사분면
        quad3 = gsum[MAX_X][y] - quad2
        # 전체에서 1,2,3 사분면 빼면 4사분면
        quad4 = gsum[MAX_X][MAX_Y] - quad1 - quad2 - quad3
        answer = min(answer, max(quad1, quad2, quad3, quad4))
    
print(answer)