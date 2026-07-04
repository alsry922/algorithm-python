n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.
# dp[i][j] = (i, j)에서 시작해서 값이 계속 커지는 방향으로 이동할 때 밟은 수 있는 최대 칸 수.
dp = [
    [1] * n for _ in range(n)
]
pos_val = [
    (i, j, grid[i][j])
    for i in range(n)
    for j in range(n)
]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
pos_val.sort(key=lambda x: -x[2])

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(nx, ny, cur_val):
    if not in_range(nx, ny):
        return False
    
    if grid[nx][ny] <= cur_val:
        return False
    
    return True

for i in range(1, n ** 2):
    sx, sy, sv = pos_val[i]
    for dx, dy in zip(dxs, dys):
        nx, ny = sx + dx, sy + dy
        if can_go(nx, ny, grid[sx][sy]):
            dp[sx][sy] = max(dp[sx][sy], dp[nx][ny] + 1)

answer = 0
for row in dp:
    answer = max(answer, *row)
print(answer)