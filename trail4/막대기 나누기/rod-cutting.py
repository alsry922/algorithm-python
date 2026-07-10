import sys
n = int(input())
profit = [0] + list(map(int, input().split()))
# INT_MIN = -sys.maxsize
# Please write your code here.
# 상태 정의를 위한 요소
#   지금까지 고려한 원소의 위치
#   지금까지 고른 막대의 길이
#   지금까지 얻은 수익
# i번째 원소까지 고려하여, 적절히 막대를 쪼갰을 때, 길이가 j인 경우 얻을 수 있는 최대 수익
# 전이식: dp[i][j] = max(dp[i-1][j], dp[i][j-i] + profit[i])
#
# 압축 가능 조건: 전이식이 참조하는 행이 i-1, i 뿐이면 1차원 압축 가능
#
# 전이식의 두 번째 항이 dp[i-1][j-i] (이전 행 참조, = 원소 재사용 불가)
#   → 1차원에서 j-i 위치가 "아직 갱신 안 된" 상태여야 함
#   → j를 큰 값 → 작은 값 순으로 순회 (역방향)
#
# 전이식의 두 번째 항이 dp[i][j-i] (현재 행 참조, = 원소 재사용 가능)
#   → 1차원에서 j-i 위치가 "이미 갱신된" 상태여야 함
#   → j를 작은 값 → 큰 값 순으로 순회 (정방향)
#
# 이 문제는 dp[i][j-i]이므로 정방향
dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j >= i:
            dp[j] = max(dp[j], dp[j - i] + profit[i])
            
print(dp[n])