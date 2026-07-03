from collections import deque
from itertools import combinations
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1
visited = [
    [False] * n for _ in range(n)
]
step = [
    [0] * n for _ in range(n)
]
wall = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 1
]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
# Please write your code here.

# bfs + 조합 완전 탐색
# bfs 시간복잡도 = O(n^2)
# n^2 중 k개를 고르는 조합 시간복잡도 = O(C(n^2, k))
# 조합마다 bfs를 수행하므로 시간복잡도 = O(C(n^2, k) * n^2)

# 벽 위치의 조합을 구해 배열에 저장
# 조합 배열을 순회하며 bfs 탐색
#   매 탐색마다 visited, step을 초기화
#   탐색 시 벽을 없애고 시작
#   탐색하며 visited, step 기록
#   탐색 종료 후 도달 시 최소 거리를 갱신
#   벽을 원래대로 복구
# 모든 조합을 순회하며 탐색했는데 한 번이라도 도달하지 못했으면 False
#   도달한 적이 있는지 변수로 관리

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 범위 안에 있고
# 방문하지 않았고
# 벽이 아니어야 함.
def can_go(x, y):
    if not in_range(x, y):
        return False
    
    return not visited[x][y] and not grid[x][y] == 1

def bfs():
    sx, sy = (r1, c1)
    ex, ey = (r2, c2)
    q = deque()
    visited[sx][sy] = True
    q.append((sx, sy))
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if not can_go(nx, ny):
                continue
            # 방문 표시
            visited[nx][ny] = True
            # step 기록
            step[nx][ny] = step[cx][cy] + 1
            # 탐색 위해 queue에 추가
            q.append((nx, ny))
        
def init():
    for x in range(n):
        for y in range(n):
            visited[x][y] = False
            step[x][y] = 0
    
def simulate(comb):
    # 벽 제거
    for x, y in comb:
        grid[x][y] = 0
    # visited, step 초기화
    init()
    # 시작점에서 bfs 시작
    bfs()
    # 벽 복원
    for x, y in comb:
        grid[x][y] = 1


reached = False
answer = 10000
for comb in combinations(wall, k):
    simulate(comb)
    if visited[r2][c2]:
        reached = True
        answer = min(answer, step[r2][c2])

print(-1 if not reached else answer)