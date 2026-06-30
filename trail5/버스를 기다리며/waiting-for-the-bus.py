N, M, C = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
# Please write your code here.
# 사람 N명, 각 사람이 정류장에 도착하는 시간 배열 t, 버스 갯수 M, 버스 최대 탑승 인원 C
# 버스가 출발할 때까지 기다리는 시간 T
# 가장 오래 기다려야 하는 사람의 최소 시간(min_wait)을 출력, 
# 버스에 사람이 다 차지 않았어도 출발 가능

# 완전탐색 가능여부 확인
# 모든 T(1 ~ 10^9)에 대해서 시도하여 min_wait을 구하면 됨
# 이미 1억이 넘음 -> 완전탐색 불가능

# 이분탐색으로 min_wait이 답이 될 수 있는 범위를 줄여나가며 답을 구할 수 있나?
# min_wait이 특정 값 미만일 때 M개의 버스에 N명의 사람들이 다 버스에 탈 수 없음.
# 반대로 특정 값 이상이면 M개의 버스에 N명의 사람들이 다 버스에 탈 수 있음.
# 단조성이 확인 됨.
# 결정함수
# min_wait을 가정했을 때 모든 사람들이 버스에 탈 수 있는가?
# 결정함수 시간복잡도 -> O(N)
# 최종 시간복잡도 O(N* log 10^9)

# 수도코드
# t 정렬
# 결정함수(min_wait):
#   first_arrive_time = t[0]
#   p_num = 1
#   departure = 0
#   t[1]부터 순회:
#     if p_num == C OR t[i] - first_arrive_time > min_wait:
#         departure += 1
#         first_arrive_time = t[i]  ← 현재 사람이 새 버스 첫 탑승자
#         p_num = 1
#     else:
#         p_num += 1
#   
#   if p_num >= 1:
#         departure += 1
#   return departure <= M

def is_possible(min_wait):
    first_arrive_time = t[0]
    p_num = 1
    departure = 0
    for i in range(1, N):
        if p_num == C or t[i] - first_arrive_time > min_wait:
            departure += 1
            first_arrive_time = t[i]
            p_num = 1
        else:
            p_num += 1
    
    if p_num >= 1:
        departure += 1
    return departure <= M

left, right = 0, 10 ** 9
answer = 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)