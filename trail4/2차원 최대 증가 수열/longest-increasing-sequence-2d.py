n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# dp[i][j] = (1, 1) ~ (i, j)까지 특정 룰을 만족하면서 점프했을 때 밟을 수 있는 칸의 최대 수
# 상태를 어떻게 정의하냐?
#   (i, j) 위치는 적어도 (i - 1)(j - 1) 위치부터 그 이전 위치에서만 점프하여 도달이 가능함.
#   dp 정의가 특정 위치까지 도달했을 때 밟을 수 있는 칸의 최대 수니까
#   dp(1, 1) ~ dp(i - 1, j - 1) 살펴보면서 최대값이 뭔지 찾아야함.
# 시간복잡도
#   dp를 채우기 위해 2차원 dp를 다 살펴보아야 하니까 O(NM)
#   dp를 채우기 위해 dp[i][j] 값을 채우기 위해 (1,1) ~ (i-1, j-1)위치를 매번 살펴보아야 하니까,
#   최종 시간복잡도 -> O(N^2 * M^2)가 되는데 값의 제한이 50 미만이므로 시간복잡도를 만족한다.

# 구현
# dp[i][j] = dp(1, 1) ~ (i - 1, j - 1)에서의 최댓값 + 1
# dp 초기화 값은 0
#   자기 자신은 무조건 밟을 수 있으니 이 칸으로 이동이 가능하면 무조건 1로 시작됨.
#   이전 칸에서 (i, j) 칸으로 이동 가능한 지 판별은 grid[i][j] > grid[0 ~ i - 1][0 ~ j - 1] 이 조건을 만족해야만 함.
#   dp[prev] 가 != 0 이 아닌 경우만 prev 위치까지 도달을 한 적이 있었다는 거니까, 이 조건을 따지면 됨
dp = [
    [0] * m for _ in range(n)
]

def init():
    dp[0][0] = 1
    for j in range(1, m):
        dp[0][j] = 0
    
    for i in range(1, n):
        dp[i][0] = 0

init()
for i in range(1, n):
    for j in range(1, m):
        v = grid[i][j]
        max_jump_cnt = 0
        for pi in range(i):
            for pj in range(j):
                # (pi, pj)에 도달한 적이 없으면 skip
                # (pi, pj)에 도달한 적이 있어도 값이 v보다 
                if dp[pi][pj] != 0 and grid[pi][pj] < v:
                    max_jump_cnt = max(max_jump_cnt, dp[pi][pj])
        if max_jump_cnt > 0:
            dp[i][j] = max_jump_cnt + 1
        # else: dp[i][j]는 0 그대로 유지 (도달 불가)

print(max(max(row) for row in dp))
