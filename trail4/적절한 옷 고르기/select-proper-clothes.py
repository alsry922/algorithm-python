N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [0] + [x[0] for x in clothes]
e = [0] + [x[1] for x in clothes]
v = [0] + [x[2] for x in clothes]
MIN = float('-inf')
# Please write your code here.
# 합산형 vs 최적화형
#   최적화형 -> dp[i]를 구하기 위해 여러 선택지 중 최선을 골라야 함
#   예를 들어, 2일차만 하더라도 1번을 두 번 입던지, 1번 2번 순으로 입던지 등 여러 선택지가 존재하고
#   그에 따라 최선의 결과를 상태값으로 저장해야 하기 때문
# 연속성 있음 vs 연속성 없음
#   "직전에 무엇을 선택했는지"가, 다음 상태를 계산하는 전이식에 반드시 필요한가 or 다음 선택지 중 못 고르게 하는 선택지가 생기는가?
#   따라서 연속성 있음.
# 재사용 허용 vs 재사용 금지
#   재사용 허용 -> 문제에서 가능하다고 나와있음

# 상태 정의에 필요한 요소:
#   몇 번째 날인지
#   마지막으로 선택한 옷 번호
#   화려함의 합
# dp는 i날까지 처리했을 때 선택한 옷이 j일 때, 얻을 수 있는 최대 화려함
dp = [[MIN] * (N + 1) for _ in range(M + 1)]
# 아무것도 안 고르면 아무것도 못 얻음
dp[0][0] = 0
def init():
    for i in range(1, N + 1):
        if s[i] <= 1 <= e[i]:
            dp[1][i] = 0

init()
for i in range(2, M + 1):
    for j in range(1, N + 1):
        # 우선 i번째 날 j번 옷을 입을 수 있는가?
        if not (s[j] <= i <= e[j]):
            # 안되면 넘어가고
            continue
        # 입을 수 있으면?
        for k in range(1, N + 1):
            if s[k] <= i - 1 <= e[k]:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(v[j] - v[k]))
        
print(max(dp[M]))