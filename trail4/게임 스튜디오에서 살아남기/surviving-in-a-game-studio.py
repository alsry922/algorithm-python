n = int(input())

# Please write your code here.
# 상태 정의에 필요한 요소
#   총 T를 받은 횟수
#   연속으로 B를 받은 횟수
# 상태 정의: i 번째 날 G, B, T를 고를 경우 살아남을 수 있는 경우의 수
B_SIZE, T_SIZE = 3, 3
MODULO_NUM = 10 ** 9 + 7
dp = [
    [
        [0] * (B_SIZE) for _ in range(T_SIZE)
    ] for _ in range(n + 1)
]

# 도착 지점을 채우기 위한 경로(출발 지점)가 항상 정해진 개수(보통 1 ~ 2개)로 고정되면  pull,
# 도착 지점을 채우려면 여러 이전 상태(출발 지점이 여러 개)가 필요하면 push
# 아무것도 안 뽑으면 경우의 수 1
dp[0][0][0] = 1
for i in range(n):
    for t in range(T_SIZE):
        for b in range(B_SIZE):
            # G를 뽑는 경우
            dp[i + 1][t][0] += dp[i][t][b]
            # T를 뽑는 경우
            if t < 2:
                dp[i + 1][t + 1][0] += dp[i][t][b]
            # B를 뽑는 경우
            if b < 2:
                dp[i + 1][t][b + 1] += dp[i][t][b]

# for i in range(1, n + 1):
#     for row in dp[i]:
#         print(row)
#     print('==========')
answer = 0
for i in range(T_SIZE):
    for j in range(B_SIZE):
        answer += (dp[n][i][j] % MODULO_NUM)

print(answer % MODULO_NUM)