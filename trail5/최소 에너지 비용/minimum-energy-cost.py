n = int(input())
dist = [0] + list(map(int, input().split())) # 장소와 장소를 이동할 때 소모하는 에너지
cost = list(map(int, input().split())) # 각 장소마다 에너지 1을 채우는데 필요한 비용(에너지 충전 비용)

# Please write your code here.
# greedy
min_cost = [0] * n # 각 장소에서의 최소 에너지 충전 비용
min_cost[0] = cost[0]
for i in range(1, n):
    min_cost[i] = min(min_cost[i - 1], cost[i])

# i -> i + 1로 이동할 때 소모 에너지와 최소 에너지 충전 비용을 계산해서 합한다.
answer = 0
for i in range(1, n):
    answer += min_cost[i - 1] * dist[i]

print(answer)