n = int(input())
dist = [0] + list(map(int, input().split()))
charge = list(map(int, input().split()))

# Please write your code here.

# 다음 위치로 이동할 때 드는 비용을 계산 
# 다음 위치로 이동할 때 현재 위치의 충전 비용과, 다음 위치의 충전 비용을 비교함.
# 다음 위치의 충전 비용이 현재 충전 비용보다 싸면 최소 충전 비용 갱신
answer = 0
min_charge = charge[0]
for i in range(1, n):
    answer += (dist[i] * min_charge)
    min_charge = min(min_charge, charge[i])

print(answer)