import sys

n, m = map(int, input().split())
quests = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
exp = [quests[i][0] for i in range(n + 1)]
time = [quests[i][1] for i in range(n + 1)]
MAX_INT = sys.maxsize
# print(quests)
# Please write your code here.
# 상태 정의를 위해 필요한 요소
#   현재까지 고려한 위치
#   경험치의 총합
#   걸린 총 시간
# 어떻게 하면 동일한 상황이 될까
#   현재까지 고려한 위치가 i로 같고,
#   경험치의 총합이 같고,
#   걸린 총 시간이 같으면, 
#   어떤 원소를 뽑았던 상관없이 같은 상황이라고 볼 수 있음.
# 상태 정의: 경험치의 총합이 a일 때, 걸린 최소 시간
# dp[i][j] = 현재까지 고려한 위치가 i이고, 경험치의 총합이 j일때 걸린 최소 시간
# dp = [
#     [MAX_INT]  * (m + 1) for _ in range(n + 1)
# ]
# dp[0][0] = 0
# for i in range(1, n + 1):
#     dp[i][0] = 0

# for i in range(1, n + 1):
#     for j in range(m + 1):
#         dp[i][j] = dp[i - 1][j]

#     for prev in range(m + 1):
#         target = min(prev + exp[i], m)
#         if dp[i - 1][prev] != MAX_INT:
#             dp[i][target] = min(dp[i][target], dp[i - 1][prev] + time[i])

# print(-1 if dp[n][m] == MAX_INT else dp[n][m])

dp = [MAX_INT] * (m + 1)
dp[0] = 0

for i in range(1, n + 1):
    for prev in range(m, -1, -1):   # 방향을 채워봐
        if dp[prev] != MAX_INT:
            target = min(prev + exp[i], m)
            dp[target] = min(dp[target], dp[prev] + time[i])

print(-1 if dp[m] == MAX_INT else dp[m])