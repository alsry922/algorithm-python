import heapq
N, T_max = map(int, input().split())
d = [int(input()) for _ in range(N)]

# Please write your code here.
# 1 <= N <= 10000
# 완전 탐색이 가능한가?
# 모든 K에 대해서 완전 탐색 진행
#   길이가 K인 배열을 선언
#   사람이 머무르는 시간을 각각 배열에 추가
#   배열이 다 차면 가장 짧은 사람을 배열에서 제거
#   추가하는 사람이 머무르는 시간은, 사람이 제거된 시간을 더해서 배열에 추가
#   이 과정은 N 명의 사람을 추가할 때마다 길이가 K인 배열을 순회하면서,
#   가장 짧은 시간을 추가해야함. O(K * N)
#   이 과정을 모든 K 에 대해 한다면 O(K * K * N)
#   아무튼 대충 겁나 큰 수가 됨. -> 불가능

# 결정함수를 정의하고 결과가 단조성을 가지게 만들 수 있나? -> 이분탐색이 가능할까?
# 후보값 K: Tmax를 넘지 않도록 할 수 있는 최소 무대 길이
# 결정함수
#   K를 가정했을 때 Tmax를 넘지 않고 모든 사람이 무대에 서고 내려가는 것이 가능한가?
#   K가 짧으면 모든 사람의 무대가 끝나는 시간이 오래걸림
#   K가 길면 모든 사람의 무대가 끝나는 시간이 짧아짐
#   특정 K값을 기준으로 성공 실패가 나누어짐 -> 단조성 확인
#   이분 탐색 사용 가능

# K길이의 배열을 선언해서 가장 짧게 머무르는 시간을 K를 순회해서 찾으면 안됨.
# O(K * N)만 해도 1억이 됨.
# 가장 짧은 값만 O(1)로 찾을 수 있을까? -> min-heap으로 구성
#   이러면 K길이의 heap에 추가 삭제는 O(log K)
#   N개에 대해서 진행하니까 O(N log K)
# O(log K) -> log 10 ^ 4 -> 약 16
# 최종 16 * 16 * N 이므로 1억번이 넘지 않으니까 시간제한 만족 가능

# k(최소 무대 길이)에 대해 이분탐색
# left, right = 1, 10000
# while left <= right:
#   mid = (left + right) // 2:
#   if is_possible(mid):
#       right = mid - 1
#   else:
#       left = mid + 1
# 결정함수(is_possible)
#   heap = []
#   for ele in d:
#       무대가 비었으면 추가
#       if len(heap) < k:
#           heapq.heappush(heap, ele)
#           continue
#       무대가 다 찾으면 가장 작은 값 빼고 새로운 값 추가
#       elapsed = heapq.heappop(heap)
#       heapq.heappush(heap, ele + elapsed)
#   모든 사람을 무대에 다 추가했음.
#   무대에 사람이 남아있으면, 가장 큰 값이 모든 사람들의 무대가 종료되는 시간이 됨.
#   return max(heap) <= Tmax

def is_possible(k):
    heap = []
    for ele in d:
        if len(heap) < k:
            heapq.heappush(heap, ele)
            continue
        elapsed = heapq.heappop(heap)
        heapq.heappush(heap, ele + elapsed)
    return max(heap) <= T_max

left, right = 1, 10000
answer = 10000
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)