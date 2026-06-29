n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

# Please write your code here.
# 완전탐색
# 물건이 모두 빠져나가는 시간의 최소시간을 모두 가정해서 시도해본다.
# 각 통로를 통괗는데 걸리는 시간이 1 ~ 10^9임.
# 모든 물건이 통과하는데 걸리는 최악의 경우 시간복잡도는 O(N * 10^9) 임.
# 엄밀하게 따지면 M개의 통로가 모두 통과하는데 걸리는 시간이 다르므로 O(N * (10^9 - M))임.
# 시간제한에 걸리게 됨.

# 후보값 t: N개의 물건이 모두 통과하는데 걸리는 시간
# t가 특정 값 이상이면 물건이 모두 통과할 수 있음, 미만이면 통과할 수 없음. -> 단조성
# 결정함수릏 세워서 이분탐색 가능
# 결정함수: t를 가정했을 때 N개의 물건이 다 통과 가능한가?
#   t를 통로가 통과하는 시간으로 나눠보면 통과 가능한 물건 갯수가 나옴
#   물건 갯수를 더했을 때 N 이상이 되는가?
#   시간복잡도 O(M)

# 수도코드
# def is_possible(t):
# arr를 순회하면서 t를 원소로 나눔.
# 나눈 몫들을 전부 더해서 N 이상인지 확인
# left, right = 1, 10 ** 9 * 10 * 5(엄밀히 따지면 arr의 최솟값 * 물건 갯수, 이 값이 상한이 되지만 편의상 이렇게 상한 정의)

def is_possible(t):
    cnt = 0
    for ele in arr:
        cnt += t // ele
    return cnt >= n

left, right = 1, 10 ** 9 * 10 ** 5
answer = 10 ** 9 * 10 ** 5
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        answer = min(answer , mid)
    else:
        left = mid + 1
    
print(answer)