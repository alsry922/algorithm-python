from itertools import combinations
from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False] * n for _ in range(n)
]
positions = [
    (i, j) for i in range(n) for j in range(n)
]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
# Please write your code here.
# bfs
# bfs 탐색 시간 복잡도는 O(n^2)
# k개의 시작점에서 bfs 시작 1 <= k <= min(n, 3)
#   시작점이 여러 곳이어도 격자는 한 번만 탐색
# k개의 시작점에서 시작하는 bfs 탐색은 O(N^2)
# 시작점 k개를 고르는 조합 C(n, k)
# 해당 조합만큼 bfs 탐색을 진행하니까
#   총 시간복잡도는 O(C(n, k) * N^2)

# 탐색 조건
#   다음 위치가 범위 안에 있어야 하고,
#   방문하지 않았어야 하고,
#   두 도시간 높이 차가 u이상 d 이하여야 함.

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, height):
    if not in_range(x, y):
        return False
    
    return not visited[x][y] and u <= abs(grid[x][y] - height) <= d
    
# # 시작점 (x, y)에서 시작하는 
def bfs(start_x, start_y):
    q = deque()
    visited[start_x][start_y] = True
    q.append((start_x, start_y))
    cnt = 1
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            # 갈 수 없으면 건너뜀
            if not can_go(nx, ny, grid[cx][cy]):
                continue
            visited[nx][ny] = True
            q.append((nx, ny))
            cnt += 1
    return cnt

components = []
for x in range(n):
    for y in range(n):
        if visited[x][y]:
            continue
        count = bfs(x, y)
        components.append(count)

components.sort(reverse=True)
print(sum(components[:k]))

# def init_visited():
#     for x in range(n):
#         for y in range(n):
#             visited[x][y] = False

# def simulation(comb):
#     init_visited()
#     count = 0
#     # 시작점마다 bfs
#     for x, y in comb:
#         if visited[x][y]:
#             continue
#         count += bfs(x, y)
#     return count

# answer = 0
# for comb in combinations(positions, k):
#     count = simulation(comb)
#     answer = max(answer, count)

# print(answer)