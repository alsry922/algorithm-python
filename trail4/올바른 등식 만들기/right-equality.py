import sys
N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

# Please write your code here.
# 상태 정의를 위해 필요한 요소
#   마지막으로 고른 원소의 위치
#   연산의 결과
# i번째 원소까지 진행했고, 서로 다른 연산을 진행한 두 가지 경우가 있을 때
# 연산의 결과가 동일하다면, 두 경우는 동일하다고 할 수 있다.
# 상태 요소를 고려해서 점화식을 세워보자.
# dp = i번째 원소를 마지막으로 골랐을 때, 연산의 결과가 j가 되도록 만들 수 있는 경우의 수
# 답을 구하는 과정 속에서 연산의 결과 k는 -20 <= k <= 20 이어야한다.
OFFSET = 20 # 연산 과정에서 -20 ~ 20으로 값의 범위가 제한되면 최종 M도 이 값의 범위를 벗어날 수 없음
dp = [
    [0] * (2 * OFFSET + 1) for _ in range(N + 1)
]
# 한 개도 뽑지 않고 연산의 결과가 0이 되는 경우의 수는 1이다.
dp[0][OFFSET] = 1
for i in range(1, N + 1):
    num = nums[i]
    for j in range(2 * OFFSET + 1):
        # num을 더했을 때 j가 되려면 dp[i - 1][j - num]이 가능했어야 함.
        if j >= num and dp[i - 1][j - num] != 0:
            dp[i][j] += dp[i - 1][j - num]
        # num을 뺏을 때 j가 되려면 dp[i - 1][j + num]이 가능했어야 함
        if j + num <= 2 * OFFSET and dp[i - 1][j + num] != 0:
            dp[i][j] += dp[i - 1][j + num]

print(dp[N][M + OFFSET])