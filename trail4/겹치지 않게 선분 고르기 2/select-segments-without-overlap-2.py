n = int(input())
segments = []
for _ in range(n):
    a, b = map(int, input().split())
    segments.append((a, b))
segments.sort()

# Please write your code here.
# 고른 두 개의 선분이 겹치지 않기 위해서는 (ax1, ax2), (bx1, bx2) 라고 했을 때
# ax2 < bx2 이거나 bx2 < ax1 이어야만 한다.
# 선분을 시작점 기준으로 정렬하면 ax2 < bx2 조건 만으로 두 선분이 겹치는지 안 겹치는지 알 수 있다.
# 그러면 상태를 어떻게 정의해야 할까?
#   i - 1번째 선분까지 고려해서 겹치지 않게 선분을 최대로 골랐을 때, i번째 선분을 뽑을 수 있을까?
#   그럼 0 ~ i - 1번째 선분을 보면서 i번째 선분의 시작점보다 작은 끝점이 하나라도 있으면 i번째 선분을 뽑을 수 있지 않을까?
#   이 방법이 예제 1, 2를 다 만족시키는 것 같음.

# dp[i] = i번째 선분까지 고려했을 때 겹치지 않게 뽑을 수 있는 최대 선분의 수
dp = [1 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    max_count = 0
    for j in range(i):
        # i의 시작점이 j의 끝점보다 큰가?
        if segments[i][0] > segments[j][1]:
            max_count = max(max_count, dp[j])
            dp[i] = max(1, max_count + 1)
print(max(dp))