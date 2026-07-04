n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [
    [0] * n for _ in range(n)
]
# Please write your code here.
# dp[i][j] = dp[i][j] = "grid[i][j]를 지나 (i,j)까지 온 모든 경로 중 최솟값의 최댓값"

def init_dp():
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], grid[i][0])
    for j in range(1, n):
        dp[0][j] = min(dp[0][j - 1], grid[0][j])

init_dp()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i - 1][j], dp[i][j - 1]), grid[i][j])

print(dp[n-1][n-1])