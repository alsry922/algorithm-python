n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
# Please write your code here.

# 가장 인접한 두 물건의 거리를 d라고 했을 때 d의 최댓값 출력
# d를 1부터 10 ** 9 까지 다 해볼 수 없음
# d가 커질수록 설치할 수 있는 물건의 갯수가 적어짐, 반대는 많아짐 -> 단조성
# 결정함수:
#   d를 가정했을 때 물건 m개를 다 설치할 수 있는가?

# 수도코드
# def is_possible(d):
# 첫 시작을 arr[0]으로 함
# 물건 갯수(cnt)는 1로 시작
# arr를 1인덱스부터 순회하면서 시작 위치 + d의 값 이상인 원소를 찾아 점을 배치하고 물건 갯수를 하나 늘림.
# 배치한 점을 시작위치로 지정하여 시뮬레이션을 계속함.
# 시뮬레이션이 끝난 후 cnt >= m 인지 판단.

# 시간복잡도
# 결정함수 O(N)
# 최종 시간복잡도 -> O(N * log 10^9)

def is_possible(d):
    last_pos = arr[0]
    cnt = 1
    for i in range(1, n):
        if last_pos + d <= arr[i]:
            last_pos = arr[i]
            cnt += 1
    
    return cnt >= m

left, right = 1, 10 ** 9
answer = 1
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)