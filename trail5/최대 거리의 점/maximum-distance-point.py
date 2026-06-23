import bisect
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# 후보값: 두 물건 사이의 거리 d
# 결정함수: 최소 거리를 d라고 가정했을 때 M개 이상의 물건을 설치할 수 있는 가?
arr.sort()
def is_possible(d):
    last_idx = 0
    cnt = 1
    for i in range(1, n):
        if arr[i] - arr[last_idx] >= d:
            last_idx = i
            cnt += 1
    return cnt >= m

lo, hi = 0, 10 ** 9
answer = 1
while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        answer = max(answer, mid)
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)
