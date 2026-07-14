n = int(input())
red = [0]
blue = [0]

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.
# 상태 정의: 마지막으로 고른 카드가 i번째이고, 지금까지 고른 빨간색 카드의 갯수가 정확히 j개일 때, 뽑힌 숫자들의 최대 합
dp = [
    [-1] * (2 * n + 1) for _ in range(2 * n + 1)
]
# 고른 카드가 없으면 합도 0임
dp[0][0] = 0
dp[1][0] = blue[1]
dp[1][1] = red[1]
for i in range(2, 2 * n + 1):
    # 빨간 카드를 하나도 안 뽑는 경우
    dp[i][0] = dp[i - 1][0] + blue[i]
    for j in range(1, 2 * n + 1):
        # i번째로 빨간 카드를 고를 수 없는 경우
        if dp[i - 1][j - 1] == -1:
            dp[i][j] = dp[i - 1][j] + blue[i]
        # i번째로 빨간 카드를 고르는 경우, i번째로 파란 카드를 고르는 경우 중 큰 거
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + red[i], dp[i - 1][j] + blue[i])
        

print(dp[2 * n][n])