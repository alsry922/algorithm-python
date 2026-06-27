from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
MAX_NUM = 1000000
# Please write your code here.
# dx, dy 테크닉을 통해 bfs 혹은 dfs 진행
# 다음으로 이동할 칸이 범위안에 있고 현재 칸과의 차이가 D 이하인 경우 이동 가능

# MAX_NUM = 1000000 = M
# 칸의 적힌 숫자는 0 ~ MAX_NUM
# D의 최솟값을 정하기 위해 일일이 0 ~ MAX_NUM 까지 bfs를 진행하는 건 
# O(M * N^2 * N^2)이니까 시간초과 발생할 수 있음(약 100조 번)

# 그렇다면 답의 범위를 이분탐색으로 좁혀가며 진행하면?
# 후보값
#   D는 색칠된 칸이 2/N이상을 만족하도록 하는 최솟값
# 결정함수
#   D가 특정 값이라고 가정했을 때, 색칠된 칸이 2/N 이상을 만족하는 경우가 존재하는가?
#   만족하는 경우 D의 값을 줄여볼 수 있고, 반대의 경우는 늘려볼 수 있음.
#   조건을 만족하는 수를 찾았을 때 최솟값(D)라면 D를 더 줄이면 조건을 만족할 수 없음.
# 그럼 grid 안에 어느 시작점을 잡아서 시작해야할까?
# 전부 한 번씩 잡아서 bfs를 시작한다면?
#   O(N^2 * N^2 * log M) -> O(N^2 * N^2 * log 10^6) -> 대충 20억번 시간 초과
# visited를 공유한다면?
#   O(N^2 * log M)이 가능 -> 약 20만번 -> 시간제한 만족 가능

# 그렇다면 최종 정리
# 결정함수
#   D를 가정했을 때 모든 지점을 대상으로 bfs를 진행했을 때
#   전체 칸을 절반이상 색칠할 수 있는 경우가 존재한다?
#   이 경우 D 값의 범위를 줄여서 다시 시도할 수 있음.

# 다음 칸이 범위 안에 있어야 함.
# 다음 칸을 방문하지 않았어야 함.
# 다음 칸과 현재 칸의 차이가 D 이하여야 함.
def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_move(cx, cy, nx, ny, visited, x):
    return is_in_range(nx, ny) and not visited[nx][ny] and abs(board[nx][ny] - board[cx][cy]) <= x

def is_possible(x):
    q = deque()
    visited = [
        [False] * n for _ in range(n)
    ]
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
    
            visited[i][j] = True
            cnt = 1
            q.append((i, j))
            while q:
                curr_v = q.popleft()
                cx, cy = curr_v
                for dx, dy in zip(dxs, dys):
                    nx, ny = cx + dx, cy + dy
                    if can_move(cx, cy, nx, ny, visited, x):
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        cnt += 1
            if cnt >= round((n ** 2 + 1) // 2):
                return True
    return False

left, right = 0, MAX_NUM
answer = MAX_NUM
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1

print(answer)