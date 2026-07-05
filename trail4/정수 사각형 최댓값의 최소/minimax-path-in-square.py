import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
INT_MAX = sys.maxsize
# Please write your code here.
# dp[i][j] = (1, 1) ~ (N, N)으로 이동했을 때 거쳐온 경로에 있는 숫자들의 최댓값 중 최솟값.
dp = [
    [INT_MAX] * n for _ in range(n)
]

def init():
    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = max(dp[0][j - 1], grid[0][j])
    
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], grid[i][0])

init()
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[n-1][n-1])
    