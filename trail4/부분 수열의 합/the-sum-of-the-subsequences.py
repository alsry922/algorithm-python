n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

# Please write your code here.
# dp[i] = 합이 i이고, 마지막으로 고른 수가 j번째 원소일 때, 만족하는 부분 수열이 존재하는지
dp = [False] * (m + 1)
# 합이 0이 되도록 하려면 안 뽑으면 됨.
dp[0] = True
for i in range(1, n + 1):
    for j in range(m, -1, -1):
        if j >= A[i]:
            if dp[j - A[i]] != False:
                dp[j] = True

print('Yes' if dp[m] else 'No')
    