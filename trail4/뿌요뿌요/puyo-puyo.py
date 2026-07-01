n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False] * n for _ in range(n)
]
# Please write your code here.
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_visit(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return True

def dfs(x, y):
    block = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_visit(nx, ny) and grid[x][y] == grid[nx][ny]:
            block += dfs(nx, ny)
    return block

exploded = 0
max_block = 0
stack = []
for x in range(n):
    for y in range(n):
        if can_visit(x, y):
            visited[x][y] = True
            stack.append((x, y))
            block = 1
            while stack:
                cx, cy = stack.pop()
                for dx, dy in zip(dxs, dys):
                    nx, ny = cx + dx, cy + dy
                    if can_visit(nx, ny) and grid[x][y] == grid[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
                        block += 1
            max_block = max(max_block, block)            
            if block >= 4:
                exploded += 1

print(exploded, max_block)
