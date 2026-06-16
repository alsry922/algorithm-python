import bisect

n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))

# Please write your code here.
stations.sort()
answer = 0
candidates = []
for fire in fires:
    # 불이 날 수 있는 위치와 가장 가까운 소방서 찾기
    lb = bisect.bisect_left(stations, fire)
    candidates = []
    # 큰 게 없는 경우
    if lb < len(stations):
        candidates.append(abs(stations[lb] - fire))
    # 크거나 같은 게 있는경우
    if lb > 0:
        candidates.append(abs(stations[lb - 1] - fire))
    
    # 이 fire에서 가장 가까운 소방서까지의 거리
    answer = max(answer, min(candidates))
    
print(answer)
