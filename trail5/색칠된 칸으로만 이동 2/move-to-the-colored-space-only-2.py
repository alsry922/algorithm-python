from collections import deque
M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]
colored = [list(map(int, input().split())) for _ in range(M)]

# Please write your code here.
# M * N 크기의 격자, 상하좌우 이동, 다음 이동 칸과의 차이가 D 이하 조건으로 bfs 진행
# 색칠된 칸끼리 이동이 가능해야 함.
# D의 최솟값을 구하라.

# 수의 범위 0 ~ 10^9를 거꾸로 순회하여 D의 최솟값을 찾는건 불가능 -> 이미 O(10^9) 는 10억임
# D를 가정했을 때 이 값이 답이 될 수 있는지 판별하는 결정함수 정의가 가능한가?
# 가능하다면 이 결정함수가 단조성을 갖는가?
# D값을 기준으로 bfs를 진행하여 답이 될수 있는지 판별 가능 -> 결정함수 O
# D값이 특정 값 이상일 때는 항상 조건을 만족 -> 단조성 O
# 그렇다면 이분 탐색으로 D가 정답이 될 수 있는 범위를 줄여나갈 수 있음.

# 결정함수:
#   특정값 D를 기준으로 bfs를 진행했을 때 D 값이 답이 될 수 있는가?
#   colored 중에 하나를 시작점으로 시작하면 됨
#   bfs의 시간복잡도는 O(M*N)
# D값의 범위는 0 ~ 10^9 -> O(logD) -> 약 35
# 총 시간복잡도는 O(M * N * log D) -> 약 35만번 -> 시간제한 만족

# 수도 코드
# colored_pos = []
# for x in range(M):
#   for y in range(N):
#       if colored[x][y] == 1:
#           colored_pos.append((x, y))

# def is_possible(d):
#   visited = M * N 크기의 2차원 배열(원소는 False)
#   sx, sy = colored_pos[0] 시작점
#   visited[sx][sy] = True 방문표시
#   q = deque bfs 큐 선언
#   q.append((sx, sy))
#   dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
#   while q: queue가 빌 때까지 진행
#       cx, cy = q.popleft() 현재 위치
#       for dx, dy in zip(dxs, dys): 
#           nx, ny = (cx + dx, cy + dy) 다음 위치
#           다음 위치가 범위 안에 있는지, 차가 d값 이내인지
#           if is_in_range(nx, ny) and abs(board[nx][ny] - board[cx][cy]) <= d and not visited[nx][ny]:
#               visited[nx][ny] = True
#               q.append((nx, ny))
#   색칠된 점을 모두 방문했는지 확인
#   for x, y in colored_pos:
#       if not visited[x][y]:
#           return False
#   return True

# left, right = 0, 10 ^ 9
# answer = right
# while left <= right:
#   mid = (left + right) // 2
#   if is_possible(mid):
#       right = mid - 1
#       answer = min(answer, mid)
#   else:
#       left = mid + 1

colored_pos = []
for x in range(M):
    for y in range(N):
        if colored[x][y] == 1:
            colored_pos.append((x, y))

def is_in_range(x, y):
    return 0 <= x < M and 0 <= y < N

def is_possible(d):
    visited = [
        [False] * N for _ in range(M)
    ]
    sx, sy = colored_pos[0]
    visited[sx][sy] = True 
    q = deque()
    q.append((sx, sy))
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys): 
            nx, ny = (cx + dx, cy + dy)
            if is_in_range(nx, ny) and abs(board[nx][ny] - board[cx][cy]) <= d and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
  
    for x, y in colored_pos:
        if not visited[x][y]:
            return False

    return True

left, right = 0, 10 ** 9
answer = right
while left <= right:
  mid = (left + right) // 2
  if is_possible(mid):
      right = mid - 1
      answer = min(answer, mid)
  else:
      left = mid + 1

print(answer)