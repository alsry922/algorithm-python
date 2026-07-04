n = int(input())

# Please write your code here.
# dp[i] = 1 ~ i까지 숫자로 만들 수 있는 서로 다른 bst 갯수(i는 노드 갯수)
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    for k in range(i):
        dp[i] += dp[k] * dp[i-1-k]

print(dp[n])