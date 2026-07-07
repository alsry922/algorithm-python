import sys
N, M = map(int, input().split())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
dp = [sys.maxsize for _ in range(M + 1)]
dp[0] = 0
for i in range(1, M + 1):
    for j in range(1, N + 1):
        if i < coin[j]:
            continue
        if dp[i - coin[j]] == -1:
            continue
        dp[i] = min(dp[i - coin[j]] + 1, dp[i])

if dp[M] == sys.maxsize:
    print(-1)
else:
    print(dp[M])