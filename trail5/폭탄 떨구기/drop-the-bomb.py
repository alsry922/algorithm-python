import bisect
n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]

# Please write your code here.
# 제일 만만한 브루트 포스 고려
#   R을 늘려가며 조건(모든 점을 제거)을 만족하는지 따져볼 수 있음
#   2 * R 크기의 윈도우를 커버되지 않은 점을 시작점으로 하여 시뮬레이션을 진행하면 됨.
#   근데 수의 범위가 0 ~ 10 ^ 9로 너무 커서 시간복잡도를 만족시킬 수 없음

# R이 특정 값 이상이면 항상 조건을 만족함, 미만이면 항상 조건을 만족할 수 없음
# 단조성이 성립함 -> 이분 탐색이 가능한 지 살펴봐야 함.
# 후보값 R: K개의 폭탄으로 모든 점을 지울 수 있도록 하는 폭발 범위값
# 결정함수: R을 가정했을 때 N 개의 점을 모두 제거할 수 있는가?
#   결정함수를 이렇게 정의하면 결정함수가 단조성을 가지므로 이분탐색 가능

# 수도코드
# 점의 위치를 정렬

# 결정 함수
# def is_possible(r):
#   2 * r 크기의 배열를 선언(윈도우)
#   배치된 폭탄 갯수는 0으로로 시작
#   시작점 a: 미커버 점 중 제일 작은 점(첫 인덱스)
#   시작점이 x[n - 1](맨 끝 점)보다 작을 때까지 반복
#   끝점 b: a + 2 * r
#   다음 시작점은 x에서 b의 upper_bound
#   배치된 폭탄 갯수를 1증가시킴
#   return 배치된 폭탄 갯수 <= k

x.sort()
def is_possible(r):
    window = 2 * r
    a = 0
    bomb_cnt = 0
    while a < n:
        a = bisect.bisect_right(x, x[a] + window)
        bomb_cnt += 1
    
    return bomb_cnt <= k

# right은 10 ^ 9 // 2로 가능하지만 그냥 편의상 10 ^ 9로 진행
# 아니네 안되네 실제로 R을 구해야하니까 R이 10 ^ 9 // 2로 시작해야 하고 그럼 10 ^ 9가 맞네
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