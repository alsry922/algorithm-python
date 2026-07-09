N, M = map(int, input().split())
coin = list(map(int, input().split()))
SNETINEL = -1
# Please write your code here.
# 상태 정의: 고른 동전의 합이 i일 때, 최대 동전 갯수
dp = [SNETINEL] * (M + 1)
# 합이 0이 되도록 동전을 고르려면 아무것도 고르지 않아야 함.
dp[0] = 0
for i in range(1, M + 1):
    for j in range(N):
        if i < coin[j]:
            continue
        if dp[i - coin[j]] == SNETINEL:
            continue
        dp[i] = max(dp[i], dp[i - coin[j]] + 1)

print(dp[M])