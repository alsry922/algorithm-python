import bisect
n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# dp[i] = 마지막으로 고른 일이 i번째 일일때, 최대로 얻을 수 있는 돈
# dp = [0] * n
# dp[0] = jobs[0][2]

# for i in range(1, n):
#     dp[i] = jobs[i][2]
#     for j in range(i):
#         if jobs[i][0] > jobs[j][1]:
#             dp[i] = max(dp[i], dp[j] + jobs[i][2])

# print(max(dp))

# 그리디로도 풀 수 있을까?
# 직관적으로 생각했을 때 일찍 끝나는 일들을 골라서 잡으면 되지 않을까?
# 이것도 교환 논증으로 가능한지 알아보자.
# 최적해 OPT가 있다고 했을 때, 최적해로 고른 원소들 중 하나를 그리디로 선택한 제일 빨리 끝나는 원소로 바꿨을 때,
# 그 값이 OPT로 고른 값이 얻는 돈보다 많다고 보장할 수 없을 것 같음

# 이진탐색으로 찾기
jobs.sort(key=lambda x: x[1])
jobs = [(-1, -1, -1)] + jobs
ends = [job[1] for job in jobs]
# dp[i] = i번째 알바까지 고려했을 때 얻을 수 있는 최대 돈
dp = [0 for _ in range(n + 1)]
dp[0] = 0
dp[1] = jobs[1][2]
for i in range(2, n + 1):
    # i번째 알바의 시작 시간보다 종료 시간이 작은 알바의 갯수
    lb = bisect.bisect_left(ends, jobs[i][0]) - 1
    # i번째 알바를 선택 하거나, 선택하지 않거나
    dp[i] = max(dp[lb] + jobs[i][2], dp[i - 1])
print(dp[n])
    