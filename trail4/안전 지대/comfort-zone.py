import sys
sys.setrecursionlimit(2500)
MAX_HEIGHT = 100
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False] * m for _ in range(n)
]
# Please write your code here.
# 안전 영역의 수가 최대가 되도록 하는 K와 안전 영역의 수를 출력
# 격자 크기 n * m -> dfs 시간복잡도는 O(n * m)
# 집의 높이 1 ~ 100 -> k의 범위
# 모든 k에 대해 dfs를 진행한다면, 시간복잡도는 O(k * n * m)
#   약 250000번 반복으로 시간 제한에 문제 없음.
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
DIR_CNT = 4

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# dfs 조건
#   다음 노드가 격자 범위 안에 있어야 함.
#   방문한 적 없어야 함
#    해당 노드 값이 k 초과

def can_visit(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return grid[x][y] > k

def dfs(x, y, k):
    for i in range(DIR_CNT):
        dx, dy = dxs[i], dys[i]
        nx, ny = x + dx, y + dy
        if can_visit(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)
    # for dx, dy in zip(dxs, dys):
        

min_k = 100
max_area = 0
for k in range(1, MAX_HEIGHT + 1):
    # visited 초기화
    for x in range(n):
        for y in range(m):
            visited[x][y] = False
    # 모든 격자에 대해 dfs 진행
    area = 0
    for x in range(n):
        for y in range(m):
            if can_visit(x, y, k):
                visited[x][y] = True
                dfs(x, y, k)
                area += 1
    
    if area == max_area:
        min_k = min(min_k, k)
    if area > max_area:
        max_area = area
        min_k = k

print(min_k, max_area)