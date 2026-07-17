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

for i in range(1, N + 1):
    for j in range(M + 1):
        # i번째 원소를 선택한 경우
        if j >= 1:
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0]) + numbers[i]
        # else문을 두지 않는 이유는 i번째 원소를 선택햇는데 구간의 갯수가 0이 될 수 없기 때문
        # i번째 원소를 선택하지 않는 경우
        dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1])

answer = MIN
for i in range(1, N + 1):
    answer = max(answer, dp[i][M][0], dp[i][M][1])

print(answer)


# i + 1 번째 원소를 선택한 경우
# if j >= 1:
#     dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j - 1][0]) + numbers[i + 1]
# # i + 1 번째 원소를 선택하지 않은 경우
# dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j][1])

# 기억해야 할 것

# "i번째 원소를 선택했을 때"라는 표현은 애매함 — 포함/미포함 여부(k)가 이미 상태 축에 있으므로, "i번째까지 처리(결정)했을 때"라고 표현해야 정확함. "선택했을 때"는 "무조건 포함된 상태"로 오독될 수 있음
# dp[i+1]을 구하는 방식과 dp[i]를 구하는 방식은 동일한 로직의 표기 차이일 뿐 — 어느 쪽이 절대적으로 편한 게 아니라, 하나로 통일해서 익숙해지는 게 실전에서 실수를 줄임
# 최댓값 DP에서 여러 출발점이 하나의 도착점으로 모이면 max()를 취함 (경우의 수 DP에서 sum을 쓰는 것과 대비됨) — 문제가 "경우의 수"인지 "최적값"인지에 따라 병합 연산자가 달라짐을 항상 확인
# 불가능한 상태 sentinel은 문제의 값 범위에 따라 결정 — 음수 포함 가능하면 float('-inf'), 양수만 가능하면 0도 가능