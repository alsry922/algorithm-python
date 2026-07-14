import sys
MIN_INT = -sys.maxsize
n, k = map(int, input().split())
numbers = [MIN_INT] + list(map(int, input().split()))


# Please write your code here.
# 상태 정의를 위한 요소
#   dp[i][j] = 마지막으로 고른 원소가 i번째 이고, 선택한 음수의 갯수가 j개인 경우 최대 합
dp = [
    [MIN_INT] * (k + 1) for _ in range(n + 1)
]
# 아무것도 안 고르고, 고른 음수의 갯수가 0이면 얻을 수 있는 합도 0임
dp[0][0] = 0
# 음수를 하나도 안 뽑는 경우 초기화
for i in range(1, n + 1):
    # 현재 수가 양수이어야만 함.
    if numbers[i] > 0:
        # 이전 원소까지 연속으로 뽑는게 가능했던 경우
        if dp[i - 1][0] != MIN_INT:
            dp[i][0] = dp[i - 1][0] + numbers[i]
        # 이전 원소까지 연속으로 뽑는게 불가능했던 경우
        else:
            dp[i][0] = numbers[i]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        # i번째 수가 음수인 경우
        if numbers[i] < 0:
            if dp[i - 1][j - 1] != MIN_INT:
                dp[i][j] = dp[i - 1][j - 1] + numbers[i]
            if j == 1:
                dp[i][j] = max(dp[i][j], numbers[i])
        # i번째 수가 양수인 경우
        else:
            if dp[i - 1][j] != MIN_INT:
                dp[i][j] = dp[i - 1][j] + numbers[i]

print(max(max(row) for row in dp[1:]))