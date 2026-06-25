from sortedcontainers import SortedList
N, T_max = map(int, input().split())
d = [int(input()) for _ in range(N)]

# Please write your code here.
# 후보값 k: 모든 사람이 무대에서 내려갈 때까지 걸리는 시간 t를 넘지 않도록 하는 최솟값
#   -> 무대에 동시에 설 수 있는 사람의 수
# k가 작아질수록 시간 t가 줄어들 수 있음. 반대로 k가 작아질수록 시간 t는 늘어남

# 결정함수
# k를 특정 값이라고 가정했을 때, 가장 오래걸리는 시간이 T_max 이하일 수 있는가?

# 시간복잡도를 O(d)로 둘 수 있는가?
# K == N 이고 매 is_possible 연산마다 범위를 반으로 줄여나감 O(logK)
# d는 100000 이므로 O(dlogK) 시간복잡도를 가진다면 시간초과가 발생하지 않음
def is_possible(k):
    if k == N:
        return True
    # k길이의 배열을 선언
    stage = SortedList()
    # d를 순회하며 stage를 채움
    # 그 다음 들어오는 사람이 stage에 머무는 시간일 계산할 때는,
    # 나간 사람의 시간을 더하여 stage에 추가
    elapsed_time = 0
    for ele in d:
        # stage가 가득 찼을 때 가장 빨리 나올 수 있는 사람을 내보냄
        if len(stage) == k:
            elapsed_time = stage[0]
            stage.remove(stage[0])
        stage.add(ele + elapsed_time)
    
    return stage[-1] <= T_max

left, right = 1, N
answer = N
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)