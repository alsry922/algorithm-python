n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False] * m for _ in range(n)
]
dxs, dys = [0, 1], [1, 0]
# Please write your code here.
# dfs 문제
# (0, 0) 에서 시작하여 조건에 해당하는 경우만 탐색을 진행하여 (n-1, m-1)에 도달할 수 있는가?
# 조건을 모두 만족해야 함.
#   (x, y)가 grid 범위 안에 있어야함.
#   visited[x][y] = False
#   grid[x][y] == 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

def dfs(cx, cy):
    for dx, dy in zip(dxs, dys):
        nx, ny = cx + dx, cy + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)

visited[0][0] = True
dfs(0, 0)
print(1 if visited[n-1][m-1] else 0)