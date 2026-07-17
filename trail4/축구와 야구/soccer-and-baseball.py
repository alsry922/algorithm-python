n = int(input())
s = [0]
b = [0]
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)
MIN = float('-inf')
B_SIZE = 9
S_SIZE = 11
# Please write your code here.
# 각 학생을 처리할 때, 이 학생을 야구팀에 넣을 지, 축구팀에 넣을 지를 결정해야 함.
# 야구팀은 9명, 축구팀은 11명임. 이거 자체가 제약 조건으로 상태 축이 될 수 있음.
# 상태 정의:
#   i번째 학생까지 처리했을 때, 야구 팀이 j명, 축구팀이 k명일 때, 능력의 최대 합
dp = [[[MIN] * (S_SIZE + 1) for _ in range(B_SIZE + 1)] for _ in range(n + 1)]

# 한 명도 뽑지 않았다면 합은 0임
dp[0][0][0] = 0
for i in range(1, n + 1):
    for j in range(B_SIZE + 1):
        for k in range(S_SIZE + 1):
            # 안 뽑는 경우
            dp[i][j][k] = dp[i - 1][j][k]
            # i번째 학생을 축구팀으로 뽑은 경우
            # i번째 학생을 야구팀으로 뽑은 경우
            if j >= 1:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + b[i])
            if k >= 1:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + s[i])

print(dp[n][B_SIZE][S_SIZE])