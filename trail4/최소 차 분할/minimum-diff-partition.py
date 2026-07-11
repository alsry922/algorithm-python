import sys
n = int(input())
arr = [0] + list(map(int, input().split()))
INT_MAX = sys.maxsize
# Please write your code here.
# N개의 수를 A, B 두 개의 그룹으로 나누어야 함.
# 각 그룹의 합의 차가 최소가 되도록 나누어야 함.
# 각 원소는 하나의 그룹에만 속할 수 있고, 각 그룹은 최소 1개 이상의 원소를 가져야 함.
# 우선 각 원소가 하나씩만 있다는 보장은 없음.
# 한 배열을 두 개의 그룹으로 나눠담기 위해서는 특정 위치를 기준으로 i번까지 A그룹, i + 1 그룹부터는 B그룹 이렇게 나누어야 함.
# 그럼 LR테크닉을 쓰면 되지 않을까?
# L = [1, i - 1]번까지의 합, R = [i, n]번 까지의 합
# 상태 정의: 특정 위치 i를 기준으로 두 그룹으로 나누었을 때의 각 그룹의 합의 최소 차
# dp[i] = min(L[i] - R[i])
# 정답은 min(dp)
# 하고보니 딱히 dp로 저장안하고 그때 그때 최솟값만 갱싱해도 될 것 같음.
# [1, 2, 3, 4] 로 예시 들면 틀림. 접근법이 틀림

# 우선 원소들을 뽑았으면 A그룹, 뽑지 않은 원소는 자연스럽게 B그룹으로 생각하면 됨.
# DFS, BFS는 연결성과 관련된 문제가 아니니까 패스
# DP 챕터니까 일단 DP를 생각
# 상태 정의를 위한 요소들
#   현재까지 고려한 위치
#   뽑은 원소들의 갯수
#   뽑은 원소들의 합
# 이 세 개가 같으면 완전히 동일한 상황임.
# 예를 들어, [1, 2, 2, 3, 5] 일때 3번 인덱스까지 고려하여 [1, 2, 3], [1, 2, 3] 이렇게 뽑으면 두 경우는 완전히 동일한 상황
# 그럼 위 요소들을 고려하여 점화식을 생각해보자
# dp[i][j] = i번째 위치까지 고려하여 원소를 골랐을 때의 합이 j가 될 수 있는지
sum_val = sum(arr)
dp = [
    [False] * (sum_val + 1) for _ in range(n + 1)
]
dp[0][0] = True
for j in range(1, sum_val + 1):
    dp[0][j] = False
for i in range(1, n + 1):
    dp[i][0] = True

for i in range(1, n + 1):
    val = arr[i]
    for j in range(1, sum_val + 1):
        # 뽑지 못한다면 뽑지 않고 j를 만들 수 있는 경우를 그대로 가져옴
        dp[i][j] = dp[i - 1][j]
        if j >= val:
            dp[i][j] = dp[i][j] or dp[i - 1][j - val]

answer = sys.maxsize
# j가 0이거나 sum_val은 두 그룹으로 나누지 못한것임.
for j in range(1, sum_val):
    if dp[n][j]:
        answer = min(answer, abs(j - (sum_val - j)))
print(answer)