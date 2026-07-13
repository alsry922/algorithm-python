n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
# 한 번에 1계단 혹은 2계단 올라갈 수 있음
# 1계단 오르는 건 최대 3번만 가능
# 상태 정의: 현재 계단 위치가 i이고, 1계단 오르는 걸 j번 했을 때, 얻을 수 있는 최대 동전 갯수
dp = [
    [-1] * 4 for _ in range(n + 1)
]
dp[0][0] = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        dp[i][0] = dp[i - 2][0] + coin[i]

for i in range(1, n + 1):
    for j in range(1, 4):
        # 1계단 올라서 i가 되는 경우
        if dp[i - 1][j - 1] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coin[i])
        # 2계단 올라서 i가 되는 경우
        if i >= 2 and dp[i - 2][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coin[i])
print(max(dp[n]))