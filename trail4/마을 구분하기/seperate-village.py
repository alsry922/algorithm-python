n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False] * n for _ in range(n)
]
village = []
# Please write your code here.
# 모든 격자에 대해 dfs 탐색 진행.
# 특정 (x, y)에서 시작해서 탐색을 계속 진행
#   탐색 할 때마다 방문 격자 갯수(사람 수)를 카운트
# 더 이상 탐색이 불가능 한 경우 하나의 마을이 됨.
# 여태 카운트한 방문 격자 갯수(사람 수)를 배열에 저장

# dfs 방문 조건
#   nx, ny 가 grid 범위 안에 있을 것
#   방문한 적이 없는 격자일 것
#   해당 격자에 벽이 없을 것

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_visit(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y]:
        return False

    return grid[x][y] == 1

# x, y를 시작점으로 dfs 탐색
def dfs(x, y):
    person = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_visit(nx, ny):
            visited[nx][ny] = True
            person += 1 + dfs(nx, ny)
    return person

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
for x in range(n):
    for y in range(n):
        if can_visit(x, y):
            # 방문 표시 후 탐색 시작
            visited[x][y] = True
            person = 1 + dfs(x, y)
            village.append(person)

village.sort()
print(len(village))
for person in village:
    print(person)