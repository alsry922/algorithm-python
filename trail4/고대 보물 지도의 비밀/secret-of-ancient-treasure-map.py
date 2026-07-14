n, k = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
MIN = float('-inf')
# Please write your code here.
# 상태 정의를 위해 필요한 요소
#   마지막으로 선택한 원소의 위치
#   지금까지 선택한 음수의 갯수
#   얻을 수 있는 연속 부분 합
# 마지막으로 선택한 원소의 위치가 i이고, 획득한 연속 부분 합이 같은 두 가지 상황이 있다면,
# 두 상황은 동일한 상황이라고 볼 수 있다.
# dp[i][j] = 마지막으로 선택한 원소의 위치가 i이고, 선택한 음수의 갯수가 j일 때, 얻을 수 있는 최대 연속 부분 합
dp = [
    [MIN] * (k + 1) for _ in range(n + 1)
]
# 하나도 한 뽑았고, 선택한 음수의 갯수도 0이면 얻을 수 있는 최대 연속 부분 합은 0이다.
dp[0][0] = 0
for i in range(1, n + 1):
    num = numbers[i]
    for j in range(k + 1):
        if num < 0:
            if j >= 1:
                dp[i][j] = dp[i - 1][j - 1] + num
                if j == 1:
                    dp[i][j] = max(dp[i][j], num)
        if num >= 0:
            dp[i][j] = dp[i - 1][j] + num
            if j == 0:
                dp[i][j] = max(dp[i][j], num)

print(max(max(row) for row in dp[1:]))