N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)
jewel = [(0, 0)] + [(weight, value) for weight, value in zip(w, v)]
SENTINEL = -1
# Please write your code here.
# 상태 정의: i번째 보석까지 고려했을 때, 무게의 합이 j(j <= M) 일 때, 보석 가치의 최대 합.
dp = [SENTINEL] * (M + 1)
# 무게가 0일때 가치도 0임
dp[0] = 0

for i in range(1, N + 1):
    weight, value = jewel[i]
    for j in range(M, -1, -1):
        if j >= weight and dp[j-weight] != SENTINEL:
            dp[j] = max(dp[j], dp[j - weight] + value)

print(max(dp))