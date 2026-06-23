n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

# Please write your code here.
# 후보값 t: 물건이 모두 통과하는데 걸리는 최소시간
# t를 가정했을 때 n개 이상의 물건이 통과할 수 있는가?

def is_possible(t):
    cnt = 0
    for ele in arr:
        cnt += (t // ele)
    return cnt >= n

left, right = 0, min(arr) * n   
answer = right
while left <= right:
    mid = (left + right) // 2
    # print(left, mid, right)
    if is_possible(mid):
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1

print(answer)
