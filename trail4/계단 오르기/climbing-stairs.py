n = int(input())
MAX_N = 1000
# Please write your code here.
dp = [0] * (MAX_N + 1)
dp[2] = 1
dp[3] = 1
for i in range(4, MAX_N + 1):
    dp[i] = (dp[i - 2] + dp[i - 3]) % 10007

print(dp[n])

# 모듈로 연산은 분배법칙 성립함
#   (a + b) % m = ((a % m) + (b % m)) % m