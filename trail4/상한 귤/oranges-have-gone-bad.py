from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False for _ in range(n)] for _ in range(n)
]
step = [
    [0] * n for _ in range(n)
]
# Please write your code here.
bad = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 2
]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y]:
        return False
    
    return grid[x][y] == 1

def bfs(bad):
    q = deque(bad)
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if not can_go(nx, ny):
                continue
            visited[nx][ny] = True
            step[nx][ny] = step[cx][cy] + 1
            q.append((nx, ny))

def simulate(bad):
    for x, y in bad:
        visited[x][y] = True
    bfs(bad)
    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                continue
            step[x][y] = -1
            if grid[x][y] == 1:
                step[x][y] = -2


simulate(bad)
for row in step:
    print(*row)