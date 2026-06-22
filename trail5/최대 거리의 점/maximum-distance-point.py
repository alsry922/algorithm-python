import bisect
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

# 가장 인접한 두 물건의 거리 d(후보값)
# d가 증가하면 배치할 수 있는 물건의 갯수가 적어짐
# 단조성 확인
arr.sort()
# print(arr)
def can_place(x):
    last_pos = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] - last_pos >= x:
            cnt += 1
            last_pos = arr[i]
    # while bisect.bisect_left(arr, last_pos + x) < len(arr):
    #     lb = bisect.bisect_left(arr, last_pos + x)
    #     last_pos = arr[lb]
    #     cnt += 1
    
    return cnt >= m


left, right = 0, arr[n - 1] - arr[0]
answer = 0
while left <= right:
    mid = (left + right) // 2
    # print(left, mid, right)
    if can_place(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)