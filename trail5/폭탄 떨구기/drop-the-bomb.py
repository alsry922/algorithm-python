n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]

# Please write your code here.
# 완전탐색 가능여부
# R 을 0 ~ 10^9 / 2 까지 전부 다 가정해서 시뮬레이션
# x를 정렬
# 시뮬레이션을 위해 2*R 크기의 윈도우를 설정
# x를 순회하며 커버되지 않은 점을 시작점(start)으로 삼고,
# 다음 위치(next)가 start + 2 * R 이내이면 해당 점도 제거됨.
# 범위 밖이면 next를 start로 잡아서 똑같이 시뮬레이션 시작.
# 시뮬레이션 완료 후의 폭탄의 갯수가 K개인지 확인하면 됨.
# 시뮬레이션은 x를 다 순회해야 하므로 O(x)
# 완전탐색의 경우 O(10^9 / 2 * N)가 되므로 시간제한에 걸림

# 이분탐색으로 답의 범위를 좁혀가며 시뮬레이션 가능한가?
# R을 가정했을 때 특정 값 이상부터는 무조건 조건을 만족, 미만은 무조건 불만족임. -> 단조성 확인
# 이분탐색이 가능하면 O(log(10^9 / 2) * N)이니까 시간제한 만족

# 수도코드
x.sort()
def is_possible(r):
    window = 2 * r
    start = x[0]
    bomb = 1
    for i in range(1, n):
        next = x[i]
        if next > start + window:
            start = next
            bomb += 1
    return bomb <= k

left, right = 0, 5 * (10 ** 8)
answer = 5 * (10 ** 8)
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)