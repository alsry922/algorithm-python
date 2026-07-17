n = int(input())

# Please write your code here.
# 상태 정의에 필요한 요소
#   총 T를 받은 횟수
#   연속으로 B를 받은 횟수
# 상태 정의: i 번째 날 G, B, T를 고를 경우 살아남을 수 있는 경우의 수
B_SIZE, T_SIZE = 3, 3
dp = [
    [
        [0] * B_SIZE for _ in range(T_SIZE)
    ]
    for _ in range(n + 1)
]
dp[0][0][0] = 1
for i in range(1, n + 1):
    for t in range(T_SIZE):
        for b in range(B_SIZE):
            if b == 0:
                dp[i][t][b] += dp[i - 1][t][0] + dp[i - 1][t][1] + dp[i - 1][t][2]
            if b == 0 and t >= 1:
                dp[i][t][b] += dp[i - 1][t - 1][0] + dp[i - 1][t - 1][1] + dp[i - 1][t - 1][2]
            if b >= 1:
                dp[i][t][b] += dp[i - 1][t][b - 1]
            dp[i][t][b] %= (10 ** 9 + 7)

answer = 0
for i in range(T_SIZE):
    answer += sum(dp[n][i]) % (10 ** 9 + 7)
print(answer % (10 ** 9 + 7))