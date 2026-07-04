n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
spos, epos = (0, n - 1), (n - 1, 0)

# dp[i][j] = (i, j)까지 이동했을 때 이동 경로에 있는 원소들의 최소 합
# dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + grid[i][j]
dp = [
    [0 for _ in range(n)] for _ in range(n)
]

def init_dp():
    dp[0][n - 1] = grid[0][n - 1]
    for j in range(n - 2, -1, -1):
        dp[0][j] = dp[0][j + 1] + grid[0][j]
    
    for i in range(1, n):
        dp[i][n - 1] = dp[i - 1][n - 1] + grid[i][n - 1]

def simulate():
    init_dp()
    for i in range(1, n):
        for j in range(n - 2, -1, -1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j + 1]) + grid[i][j]

simulate()
print(dp[n - 1][0])
