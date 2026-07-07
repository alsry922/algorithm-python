n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# dp[i] = 마지막으로 고른 일이 i번째 일일때, 최대로 얻을 수 있는 돈
dp = [0] * n
dp[0] = jobs[0][2]

for i in range(1, n):
    dp[i] = jobs[i][2]
    for j in range(i):
        if jobs[i][0] > jobs[j][1]:
            dp[i] = max(dp[i], dp[j] + jobs[i][2])

print(max(dp))