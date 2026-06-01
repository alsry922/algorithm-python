import sys
n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
MAX = sys.maxsize
# Please write your code here.
# 각 장소에서 맨 오른쪽 장소까지 이동하는데 드는 에너지

min_so_far = cost[0]
total = dist[0] * cost[0]

for i in range(1, n - 1):
    min_so_far = min(min_so_far, cost[i])
    total += dist[i] * min_so_far

print(total)