N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
OFFSET = 20
# Please write your code here.
# 상태 정의에 필요한 요소
#   마지막으로 선택한 요소
#   계산 결과
# 마지막으로 선택한 요소가 i번째일 때, 계산 결과를 j를 만들 수 있는 경우의 수
dp = [
    [0] * (2 * OFFSET + 1) for _ in range(N + 1)
]
# 아무것도 안 뽑고 0이 되는 경우의 수는 1개
dp[0][OFFSET] = 1
for i in range(1, N + 1):
    num = nums[i]
    for j in range(2 * OFFSET + 1):
        # dp[i][j] 를 계산하기 위해서 고려할 요소
        # i번째 원소를 빼서 j가 된 경우
        #   dp[i - 1][j + num]의 경우에서 num 뺀 경우임
        # i번째 원소를 더해서 j가 된 경우
        #   dp[i - 1][j - num]의 경우에서 num을 더하는 경우
        if j + num <= 2 * OFFSET:
            dp[i][j] += dp[i - 1][j + num]
        if j >= num:
            dp[i][j] += dp[i - 1][j - num]

print(dp[N][M + OFFSET])