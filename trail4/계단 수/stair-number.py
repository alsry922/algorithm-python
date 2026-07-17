n = int(input())
NUM = 9
MOD = 10 ** 9 + 7
# Please write your code here.
# 합산형 vs 최적화형
#   조건에 따라 최선의 상태를 구할 필요 없음
#   가능한 갯수를 구하면 됨. 합산형
# 연속성 있음 vs 없음
#   연속성 있음. 이전 수를 뭘 선택했느냐에 따라 다음에 선택할 수 있는 수가 정해짐.
# 재사용 가능 vs 불가
#   재사용 가능. 이전에 사용된 숫자는 다시 사용될 수 있음

# 상태 정의:
#   dp = 계단 길이가 i일 때, j수를 골랐을 때 만들 수 있는 계단 수의 갯수
dp = [[0] * (NUM + 1) for _ in range(n + 1)]
# 계단 길이가 0이고, 아무것도 안 뽑는 경우(공집합)
dp[0][0] = 1
def init():
    for i in range(1, NUM + 1):
        dp[1][i] = 1

init()
for i in range(2, n + 1):
    for j in range(NUM + 1):
        # j번 수를 뽑으려면
        # i - 1번에서 j - 1 혹은 j + 1을 골랐어야 함.
        if j - 1 >= 0:
            dp[i][j] += (dp[i - 1][j - 1] % MOD) 
        if j + 1 <= NUM:
            dp[i][j] += (dp[i - 1][j + 1] % MOD)

# for row in dp:
#     print(row)
print(sum(dp[n]) % MOD)
