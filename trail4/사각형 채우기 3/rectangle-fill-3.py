n = int(input())
A = [0] * (n + 1)
B = [0] * (n + 1)
MOD = 1000000007
# Please write your code here.
A[0] = 1
A[1] = 2
B[0] = 0
B[1] = 0
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 2
for i in range(2, n + 1):
    B[i] = (2 * A[i-2] + B[i-1]) % MOD
    A[i] = (2 * A[i-1] + B[i] + A[i-2]) % MOD
    dp[i] = A[i]
print(dp[n])