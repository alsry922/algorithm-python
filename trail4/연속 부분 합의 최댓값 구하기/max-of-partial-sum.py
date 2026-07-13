import sys
n = int(input())
arr = list(map(int, input().split()))
MIN_INT = -sys.maxsize
# Please write your code here.
# 상태정의: 마지막으로 고른 위치가 i일 때, 얻을 수 있는 최대 합
dp = [MIN_INT] * (n)
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))