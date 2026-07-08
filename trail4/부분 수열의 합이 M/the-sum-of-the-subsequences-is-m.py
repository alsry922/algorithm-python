import sys
n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
INT_MAX = sys.maxsize
# Please write your code here.
# 수열 A의 부분 수열 내 원소의 합이 M이 되도록 하는 최단 부분 수열 길이
# 상태 정의: 선택한 부분수열의 합이 i이고, 마지막으로 선택한 원소가 j번째 일 때, 최단 부분 수열 길이
# 상태를 뒤집어서 정의하면?
#   마지막으로 선택한 원소가 i일 이고, 부분수열의 합이 j일 때, 최단 부분 수열의 길이.

dp = [sys.maxsize] * (m + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(m, -1, -1):
        # i번째 원소를 골라서 합이 j가 되려면 뺐을 때 0 이상이어야 함.
        if j >= A[i]:
            # print(A[i], j, dp[j], dp[j - A[i]])
            if dp[j - A[i]] == INT_MAX:
                continue
            dp[j] = min(dp[j], dp[j - A[i]] + 1)
answer = dp[m]
if answer == INT_MAX:
    answer = -1
print(answer)