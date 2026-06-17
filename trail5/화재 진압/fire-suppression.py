n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))

# Please write your code here.
# fires, stations를 정렬
# i, j 투 포인터를 잡음
# i를 증가시킬 때 j를 감소시키면 거리가 더 멀이지기 때문에 j를 유지 혹은 증가시켜야함.
# 화재 발생 위치 i에서 stations[j] 까지의 거리보다
#   stations[j + 1] 까지의 거리가 더 짧으면 j를 증가시킨다.
def dist(i, j):
    return abs(fires[i] - stations[j])

fires = [0] + sorted(fires)
stations = [0] + sorted(stations)
j = 1
answer = 0
for i in range(1, n + 1):
    while j + 1 <= m and dist(i, j) > dist(i, j + 1):
        j += 1
    
    answer = max(answer, dist(i, j))

print(answer)