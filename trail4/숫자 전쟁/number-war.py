n = int(input())
first_cards = [0] + list(map(int, input().split()))
second_cards = [0] + list(map(int, input().split()))

# Please write your code here.
# 두 사람이 카드 게임을 함
# 카드에 적힌 숫자가 적은 쪽이 숫자만큼 점수를 얻고 카드를 버림
# 한 명의 카드가 모두 소진될 때까지 게임을 함.
# 상태 정의를 위해 필요한 요소
#   상대 카드의 위치
#   남우 카드의 위치
# 상태정의를 어떻게 해야하지?
#   현재 상대 카드의 위치가 i이고 남우 카드의 위치가 j일때 남우가 얻을 수 있는 최대 점수?
dp = [
    [-1] * (n + 2) for _ in range(n + 2)
]
dp[1][1] = 0
for i in range(1, n + 2):
    for j in range(1, n + 2):
        if i > n or j > n:
            continue
        if dp[i][j] == -1:
            continue
        cur = dp[i][j]
        # 카드 버리기
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], cur)
        if first_cards[i] > second_cards[j]:
            dp[i][j + 1] = max(dp[i][j + 1], cur + second_cards[j])
        elif first_cards[i] < second_cards[j]:
            dp[i + 1][j] = max(dp[i + 1][j], cur)
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], cur)


print(max(max(dp[n + 1]), max(dp[i][n + 1] for i in range(n + 2))))