import sys

n, m = map(int, input().split())
quests = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
exp = [quests[i][0] for i in range(n + 1)]
time = [quests[i][1] for i in range(n + 1)]
MAX_INT = sys.maxsize
MAX_T = sum(time)
# 상태 정의:
#   dp[i][j] = 현재까지 고려한 원소의 위치가 i이고, 총 걸린 시간이 j일 때 얻은 경험치의 합
dp = [
    [-1] * (MAX_T + 1) for _ in range(n + 1)
]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(MAX_T + 1):
        # i번째 원소를 뽑지 못하는 경우 dp[i-1][j] 값을 이어받아야 함.
        dp[i][j] = dp[i - 1][j]
        # j 시간이 i번째 원소의 시간보다 크거나 같은 경우에 i번째 원소를 뽑을 수 있음
        if j >= time[i] and dp[i - 1][j - time[i]] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - time[i]] + exp[i])

answer = MAX_T + 1
for i in range(MAX_T + 1):
    # 총 경험치 합이 m 이상이어야 함.
    if dp[n][i] >= m:
        answer = min(answer, i)

print(-1 if answer == MAX_T + 1 else answer)