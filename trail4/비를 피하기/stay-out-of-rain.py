from collections import deque
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False] * n for _ in range(n)
]
step = [
    [0] * n for _ in range(n)
]
answer = [
    [0] * n for _ in range(n)
]
shelter = [
    (i, j) 
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 3
]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
# Please write your code here.
# 가중치가 같은 격자에서 최소 이동 거리 = bfs
# 모든 격자를 살펴보며 사람이 서있는 격자에서만 bfs 시작
# bfs 시작 조건
#   사람이 있어야 하고,
#   방문하지 않은 격자여야 함.
# bfs 탐색 조건
#   다음 위치가 범위 안에 있어야 함.
#   방문한 곳이 아니어야 함.
#   벽(1)이 아니어야 함.

# visited 2차원 배열 = 해당 위치를 방문했는지 기록
# step 2차원 배열 = shelter 위치까지 가기 위한 최소 이동거리 기록
# answer 2차원 배열 = 각 시작점에서 shelter까지 가기 위한 최소 이동 거리를 시작점에 기록
# 모든 격자를 순회하며 사람이 서있는 격자에서만 bfs 시작
#   매 시작점마다 visited, step을 초기화
#   시작점에서 bfs 진행 후, shelter 위치의 step 값을 비교하여 최솟값을 찾아 answer 2차원 배열의 시작점 위치에 기록
# 이러면 O(n^4) 시간복잡도 초과

# 모든 격자를 순회하며 shelter가 있는 격자에서 bfs 시작
#   이렇게 하면 shelter 사람이 있는 위치까지 갈 수 잇는 최단 거리를 구할 수 있음.
#   이렇게 하면 사람 위치마다 bfs를 돌지 않고 한 번의 bfs로 각 최단거리를 구할 수 있음.

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 범위 안에 있어야 하고
# 방문하지 않았어야 하고
# 벽이 아니어야 함.
def can_go(x, y):
    if not in_range(x, y):
        return False

    return not visited[x][y] and not grid[x][y] == 1

def bfs(start_positions):
    q = deque()
    for x, y in start_positions:
        visited[x][y] = True
        q.append((x, y, 0))
    while q:
        cx, cy, cstep = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny, nstep = cx + dx, cy + dy, cstep + 1
            if not can_go(nx, ny):
                continue
            visited[nx][ny] = True
            q.append((nx, ny, nstep))
            if grid[nx][ny] == 2:
                step[nx][ny] = nstep
bfs(shelter)
for x in range(n):
    for y in range(n):
        if grid[x][y] == 2 and step[x][y] == 0:
            step[x][y] = -1

for row in step:
    print(*row)