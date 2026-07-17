N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
MIN = float('-inf')
# Please write your code here.
# 상태 정의를 위해 필요한 요소
#   마지막으로 살펴본 원소의 위치(현재 위치)
#   구간의 갯수
#   현재 원소를 포함할건지 말건지
# dp[i][j][k] = i번째 원소까지 처리했을 때, 구간의 갯수가 j개이고, 현재 원소를 선택할지 말지 여부를 k라 했을 때 최대합
dp = [[[MIN] * (2) for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
# dp[0][0][1] 은 가능하지 않음

for i in range(N):
    for j in range(M + 1):
        # i + 1 번째 원소를 선택한 경우
        if j >= 1:
            dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j - 1][0]) + numbers[i + 1]
        # i + 1 번째 원소를 선택하지 않은 경우
        dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j][1])

answer = MIN
for i in range(1, N + 1):
    answer = max(answer, dp[i][M][0], dp[i][M][1])

print(answer)