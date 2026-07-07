n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
# 하나의 상태로 정의할 수는 없을 것 같음.
# dp[i][j] = 마지막으로 고른 원소의 취이가 i이면서,
# 현재 증가-감소 상태가 j일때(증가하는 중이면 j = 0, 감소하는 중이면 j = 1)
# 부분 수열 중 최장 증가-감소 부분 수열의 길이

dp = [
    [1 for _ in range(n)] for _ in range(n)
]

for i in range(1, n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        if sequence[i] < sequence[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)
    dp[i][1] = max(dp[i][0], dp[i][1])

print(max(max(row) for row in dp))