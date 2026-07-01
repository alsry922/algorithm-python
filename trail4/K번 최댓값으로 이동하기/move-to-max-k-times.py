from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
visited = [
    [False] * n for _ in range(n)
]
NOT_EXISTS = (-1, -1)
# Please write your code here.
# bfs + 완전탐색
# n ^ 2 순회하며 bfs
# bfs 한 번 수행 후 최댓값 위치를 찾기 위해 n ^ 2를 또 순회하며, 조건에 맞는 위치 판단
# 이를 k번 수행하고 수행하니까
# O(k * (n^2 + n^2)) = O(k * n^2) == O(n ^ 3) -> 시간복잡도 만족

# 시작 위치 기준으로 bfs 탐색 진행
# bfs 후에 이동을 했는지 안 했는지를 판단
#   최적 위치를 센티넬로 선언하고 bfs 진행 후에 최적 위치가 시작 위치면 이동하지 않은 것임.

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 이동 가능 조건
#   범위 안에 있어야 하고,
#   방문하지 않았어야 하고,
#   시작 위치의 값보다 작아야 함.
def can_go(nx, ny, cur_val):
    if not in_range(nx, ny):
        return False
    
    return not visited[nx][ny] and grid[nx][ny] < cur_val

# start_x, start_y에서 시작해서 이동했는지 판단
# def is_moved(start_x, start_y):

# 최적 위치 업데이트가 필요한지
def need_best_pos_update(best_pos, new_pos):
    if best_pos == NOT_EXISTS:
        return True
    
    best_x, best_y = best_pos
    new_x, new_y = new_pos
    return (grid[best_x][best_y], -best_x, -best_y) < (grid[new_x][new_y], -new_x, -new_y)
            

def bfs(start_x, start_y):
    q = deque()
    # 시작 위치 방문 표시
    visited[start_x][start_y] = True
    # 시작 위치 큐에 추가
    q.append((start_x, start_y))
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        cx, cy = q.popleft()    
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            # 방문 가능하지 않으면 넘어감
            if not can_go(nx, ny, grid[start_x][start_y]):
                continue
            # 방문 표시
            visited[nx][ny] = True
            # 큐에 추가
            q.append((nx, ny))


def initialize_visited():
    for x in range(n):
        for y in range(n):
            visited[x][y] = False

# start_x, start_y에서 시작하여 탐색 시도
# 최적 위치를 반환
def move_start(start_x, start_y):
    # visited 초기화
    initialize_visited()
    # bfs 수행
    bfs(start_x, start_y)
    # 최적 위치 구하기
    best_pos = NOT_EXISTS
    for x in range(n):
        for y in range(n):
            # 방문 안 한 곳과 시작 위치는 넘어감
            if not visited[x][y] or (x, y) == (start_x, start_y):
                continue
            new_pos = (x, y)
            if need_best_pos_update(best_pos, new_pos):
                best_pos = new_pos
    return best_pos

curr_v = (r - 1, c - 1)
for _ in range(k):
    cx, cy = curr_v
    # 최적 위치
    best_pos = move_start(cx, cy)
    # 이동하지 않았으면(최적 위치 찾기 불가능)
    if best_pos == NOT_EXISTS:
        break
    # 최적위치 찾았으면 다음 이동 준비
    curr_v = best_pos
    
print(curr_v[0] + 1, curr_v[1] + 1)