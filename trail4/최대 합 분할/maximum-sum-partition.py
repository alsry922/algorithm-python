n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# 상태 정의
# dp[i][j] = i번째까지 고려하여 A 그룹을 뽑았을 때 sum(A) - sum(B)가 j가 되는 경우들 중 sum(A)의 최댓값
sum_val = sum(arr)
OFFSET = sum_val
dp = [
    [-1] * (OFFSET + sum_val + 1) for _ in range(n + 1)
]
# 0번째까지 고려(안 뽑음)
# d가 0이 되는 경우
# 이 중 sum(A)의 최댓값
dp[0][OFFSET] = 0
for i in range(1, n + 1):
    for j in range(OFFSET + sum_val + 1):
        if j >= arr[i] and dp[i - 1][j - arr[i]] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - arr[i]] + arr[i])
        if j + arr[i] <= 2 * sum_val and dp[i - 1][j + arr[i]] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j + arr[i]])
        if dp[i - 1][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

answer = dp[n][OFFSET]
print(answer)
