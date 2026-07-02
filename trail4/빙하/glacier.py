from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False] * m for _ in range(n)
]
# Please write your code here.
# bfs + 완전 탐색이 가능한가?
# 제일 바깥 족은 다 물이니까 시작점을 (0, 0) 으로 시작해서 bfs 시작
# 탐색 조건
#   다음 위치가 범위안에 있어야 함.
#   다음 위치가 0이어야 함.
# 탐색하면서 다음 위치가 물인 경우
#   해당 다음 위치를 방문 표시하고 q에 넣음
# 탐색하면서 다음 위치가 빙하인 경우
#   해당 다음 위치의 값을 0으로 바꾸고 방문 표시를 함.
#   q에 넣지는 않음.
#   0으로 바꾼 횟수를 count해서 저장
# 더 이상 방문하지 않은 곳이 없다면 마지막 시뮬레이션에서 저장한 count가 정답

# 총 시간복잡도는 O(min(n * m) * n * m)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    return not visited[x][y] and grid[x][y] == 0

def can_melt(x, y):
    if not in_range(x, y):
        return False
    
    return not visited[x][y] and grid[x][y] == 1


def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

# bfs 탐색 후 녹은 빙하 수 반환
def bfs(x, y):
    initialize_visited()
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    melted_count = 0
    q = deque()
    visited[x][y] = True
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_melt(nx, ny):
                visited[nx][ny] = True
                grid[nx][ny] = 0
                melted_count += 1
            elif can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
    return melted_count


time = 0
last_melted_cnt = 0
while True:
    melted_count = bfs(0, 0)
    if melted_count == 0:
        break
    time += 1
    last_melted_cnt = melted_count

print(time, last_melted_cnt)