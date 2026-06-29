from collections import deque

M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]
colored = [list(map(int, input().split())) for _ in range(M)]
colored = [(i, j) for i in range(M) for j in range(N) if colored[i][j] == 1] 
visited = [
    [False] * N for _ in range(M)
]
# Please write your code here.
# 격자에서의 bfs
# 이동 가능 조건: 상하좌우로 and 미방문 and 현재 위치의 값과 다음 위치의 값 차이가 D 이하
# 색칠된 칸끼리 이동가능하다록 하는 D의 최솟값 출력

# 완전탐색 가능?
# 수의 범위가 0 ~ 10^9임. D의 범위도 마찬가지이므로 범위가 너무큼.
# 모든 가능한 D에 대해 완전탐색을 하는 건 시간복잡도를 만족시킬 수 없음.
# 완전탐색 불가능

# 조건: bfs를 진행할 떄 색칠된 칸은 모두 방문 가능해야함.
# D의 값이 작아질수록 이동할 수 있는 칸의 수가 적어짐 -> 조건 불만족할 수 있음.
# D가 특정 값 이상이면 항상 조건을 만족함. 미만이면 조건을 항상 만족할 수 없음
# 단조성이 있음. -> 이분탐색 가능 -> 결정함수를 단조성에 맞춰 설계
# 결정함수: 특정 D값을 가정했을 때 조건을 만족할 수 있는가?
# 결정함수는 O(N * M) -> bfs 시간복잡도
# 이분탐색 O(log 10^9) -> 약 30번
# 최종 시간복잡도는 O(N * M * log 10 ^ 9)


# 수도코드
# 결정함수
# def is_possible(d):
# visited 2차원 배열 선언
# queue 선언
# 시작 위치 queue 삽입 및 방문표시
# bfs 진행
# bfs 종료 후 색칠된 칸 모두 방문했는지를 확인 후 return

# bfs
# queue를 다 소모할 때까지 진행
# 상하좌우를 살펴보며 방문 가능한 위치인지 판단
# 방문 가능하다면 해당 위치를 방문 표시 및 queue에 삽입

# 방문 가능 판별 함수

# 범위 안에 있는지, 미방문 위치인지
# return in_range(x, y) and not visited[x][y] and abs(board[x][y] - board[nx][ny]) <= d

# 범위 판별 함수
# def in_range(x, y):
# return 0 <= x < M and 0 <= y < N

def in_range(x, y):
    return 0 <= x < M and 0 <= y < N

def is_possible(d):
    # 방문표시 초기화
    for i in range(M):
        for j in range(N):
            visited[i][j] = False
    # queue 선언
    q = deque()
    # 시작 위치 추가 및 방문 표시
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    # bfs 시작
    vx, vy = colored[0]
    q.append((vx, vy))
    visited[vx][vy] = True
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            # nx, ny가 범위 안에 있고, 방문하지 않았으며, 현재 위치의 값과의 차이가 d이내인 경우
            if in_range(nx, ny) and not visited[nx][ny] and abs(board[nx][ny] - board[cx][cy]) <= d:
                # 방문 표시 및 queue에 추가
                visited[nx][ny] = True
                q.append((nx, ny))

    for x, y in colored:
        if not visited[x][y]:
            return False
    return True

left, right = 0, 10 ** 9
answer = 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)