import sys
n = int(input())
profit = [0] + list(map(int, input().split()))
# INT_MIN = -sys.maxsize
# Please write your code here.
# 상태 정의를 위한 요소
#   지금까지 고려한 원소의 위치
#   지금까지 고른 막대의 길이
#   지금까지 얻은 수익
# i번째 원소까지 고려하여, 적절히 막대를 쪼갰을 때, 길이가 j인 경우 얻을 수 있는 최대 수익
dp = [
    [0] * (n + 1) for _ in range(n + 1)
]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # i번째 원소를 사용하지 않고, 길이가 j인경우
        # i번째 원소를 사용하고 길이가 j - i인 경우
        if j >= i:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - i] + profit[i])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][n])
