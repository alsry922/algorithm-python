n = int(input())
MAX_N = 1000
# Please write your code here.
dp = [0] * (MAX_N + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, MAX_N + 1):
    dp[i] = (dp[i- 1] + dp[i - 2]) % 10007

print(dp[n])