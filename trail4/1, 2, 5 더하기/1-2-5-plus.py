n = int(input())
arr = [0, 1, 2, 5]
length = len(arr)
# Please write your code here.
# 상태 정의
#   합 i를 만들기 위해 마지막으로 고른 원소가 j번째 원소인 경우의 수?
#   i번째 원소들 중, 일부를 선택해서 합이 j가 되는 경우의 수?
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    for j in range(1, length):
        if i >= arr[j]:
            dp[i] += dp[i - arr[j]]
            dp[i] %= 10007

print(dp[n])
        