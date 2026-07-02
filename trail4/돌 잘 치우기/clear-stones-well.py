from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
n, k, m = list(map(int, input().split()))
grid = [
    list(map(int, input().split())) for _ in range(n)
]
visited = [
    [False] * n for _ in range(n)
]
start_pos = []
for _ in range(k):
    r, c = map(int, input().split())
    start_pos.append((r - 1, c - 1))
# Please write your code here.
# bfs
# M개의 돌을 적절하게 치워 K개의 시작점으로부터 bfs 탐색했을 때
# 도달가능한 칸의 최대 수를 출력
# 탐색 조건
#   다음 위치가 격자 범위 안에 있을 것
#   다음 위치에 돌이 없을 것

# bfs + 완전탐색(backtracking) 가능한가?
# 시간복잡도
# bfs = O(n^2)
#   k개의 시작점에서 시작하더라도 이미 방문한 곳은 방문하지 않으니까 O(n^2)
# m은 최대 8이하.
#   최대 8개의 자리에 대해 뽑거나 뽑지 않거나를 진행
#   2 ^ 8
# 최종 시간 복잡도 = O(2^m * n^2)는 1억을 넘지 않음 -> 따라서 가능

# grid를 순회하며 돌의 위치를 저장
# C(초기 입력에서 돌의 갯수, m) 를 구하고,
# 각 위치에서 돌을 치움(0으로 만듦)
# 시작점에서 bfs 시작
#   도달가능한 칸의 캣수를 세고, max_count를 갱신
# 치웠던 돌을 다시 원상복구
# max_count 출력

def can_go(x, y):
    # 범위를 벗어남
    if not (0 <= x < n and 0 <= y < n):
        return False
    # 방문하지 않은 점이며, 돌이 없어야 함.
    return not visited[x][y] and grid[x][y] != 1

# 시작위치 기준 bfs 탐색 후 방문가능한 영역 수를 반환
def bfs(start_pos):
    cnt = 0
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for x, y in start_pos:
        if visited[x][y]:
            continue
        q = deque()
        visited[x][y] = True
        q.append((x, y))
        cnt += 1
        while q:
            cx, cy = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = cx + dx, cy + dy
                if not can_go(nx, ny):
                    continue
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt


def initialize_visited():
    for x in range(n):
        for y in range(n):
            visited[x][y] = False

def simulation(comb):
    comb = list(comb)
    # visited 초기화
    initialize_visited()
    # 돌 치우기
    for x, y in comb:
        grid[x][y] = 0
    # 탐색 후 영역 갯수 저장
    cnt = bfs(start_pos)
    # 돌 다시 놓기
    for x, y in comb:
        grid[x][y] = 1
    return cnt

# 돌 위치 저장
stone = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stone.append((i, j))
max_cnt = 0
for comb in combinations(stone, m):
    cnt = simulation(comb)
    max_cnt = max(max_cnt, cnt)

print(max_cnt)