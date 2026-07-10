N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = [0] + list(w), [0] + list(v)

# Please write your code here.
# 상태 정의에 필요한 요소
#   현재까지 고려한 원소의 위치
#   고른 보석들의 무게의 합
#   고른 보석들의 가치의 합
# 상태 정의: 현재까지 고려한 원소의 위치가 i이고, 보석을 적절히 골랐을 때, 무게의 합이 j 이하일 때, 최대 가치
dp = [
    [-1] * (M + 1) for _ in range(N + 1)
]
dp[0][0] = 0
for i in range(1, N + 1):
    dp[i][0] = 0

for j in range(1, M + 1):
    dp[0][j] = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # 뽑을 수 없는 경우는 이전 행의 값을 가져와야 함.
        dp[i][j] = dp[i - 1][j]
        # 해당 보석을 뽑으려면 목표 무게가 현재 뽑으려는 보석 무게보다 커야함
        # 이 보석을 뽑아서 목표 무게를 만들려면, 이 보석을 뽑기 전 상태에 값이 있어야 함.
        if j >= w[i]:
            dp[i][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])

print(max(dp[N]))


