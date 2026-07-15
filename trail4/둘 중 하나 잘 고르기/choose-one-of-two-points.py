MIN = float('-inf')
MAX = float('inf')
n = int(input())
red = [0]
blue = [0]
pn = 2 * n
for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.
# 상태 정의를 위해 필요한 요소
#   게임을 진행한 횟수
#   고른 빨간색 카드 갯수
#   뽑힌 숫자들의 합
# 지금까지 게임을 진행한 횟수가 i이고, 빨간색 카드를 j개 골랐을 때 뽑은 숫자들의 합은 클수록 좋다.
# dp[i][j] = i번 게임을 진행했고, 고른 빨간색 카드 갯수가 j개일 때, 고른 숫자들의 최대 합.
# 합을 구하는 거고, 각 원소는 1 이상이니까 0은 절대 답이 될 수 없음. 센티넬로 사용 가능
dp = [
    [MIN] * (pn + 1) for _ in range(pn + 1)
]
# 아무것도 고르지 않고, 빨간색 카드 갯수가 0인 경우, 합은 0임
dp[0][0] = 0

def init():
    # 빨간색만 고르는 경우
    for i in range(1, pn + 1):
        dp[i][i] = dp[i - 1][i - 1] + red[i]
    # 파란색만 고르는 경우
    for j in range(1, pn + 1):
        dp[j][0] = dp[j - 1][0] + blue[j]
init()

for i in range(2, pn + 1):
    r, b = red[i], blue[i]
    for j in range(1, pn + 1):
        # i번째까지 진행한 했을 때, 빨간색 카드를 j개 골랐다면,
        # i - 1 번째까지 빨간색을 j - 1 고르고 i번째에 빨간색을 고른 경우,
        # i - 1 번째까지 이미 빨간색을 j 개 골랐고 i뻔째에 파란색을 고른 경우,
        # 둘 중 큰 값이 목표값이다.
        dp[i][j] = max(dp[i - 1][j - 1] + r, dp[i - 1][j] + b)

print(dp[pn][n])
