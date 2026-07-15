n, k = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
MIN = float('-inf')
# Please write your code here.
# 상태 정의에 필요한 요소
#   마지막으로 선택한 원소의 위치
#   현재까지 선택한 음수의 갯수
#   얻은 수 있는 총합
# dp[i][j] = 마지막으로 선택한 원소의 위치가 i이고, 선택한 음수의 갯수가 j개 일 때, 얻을 수 있는 최대 합
dp = [
    [MIN] * (k + 1) for _ in range(n + 1)
]
# 아무것도 뽑지 않으면 합은 0임.
dp[0][0] = 0
# 1번째 수가 양수면 dp[1][0]만 가능, 음수면 dp[1][1]만 가능
if numbers[1] >= 0:
    dp[1][0] = numbers[1]
else:
    dp[1][1] = numbers[1]
for i in range(2, n + 1):
    num = numbers[i]
    # num이 양수인 경우 
    if num >= 0:
        # 음수의 갯수가 0이면 이전 상태에서 이어 붙이거나, i번째 수부터 시작할 수 있음
        dp[i][0] = max(dp[i - 1][0] + numbers[i], numbers[i])
        for j in range(1, k + 1):
            # i를 뽑아서 음수의 갯수를 j개를 만들어야 하니까.
            # 음수의 갯수가 1이상이면 이전 상태에서 이어붙여야 함.
            # 이전 상태가 유효한 경우에 이어붙일 수 있음
            if dp[i - 1][j] != MIN:
                dp[i][j] = dp[i - 1][j] + numbers[i]
    
    # num이 음수인 경우
    else:
        # 음수의 갯수가 1이면 이전 상태에서 이어 붙이거나, i번째 수부터 시작할 수 있음
        dp[i][1] = max(dp[i - 1][0] + numbers[i], numbers[i])
        for j in range(2, k + 1):
            if dp[i - 1][j - 1] != MIN:
                dp[i][j] = dp[i - 1][j - 1] + numbers[i]

print(max(max(row) for row in dp[1:]))