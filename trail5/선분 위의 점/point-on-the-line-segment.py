n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def lower_bound(target):
    left, right = 0, n - 1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if target <= points[mid]:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

def upper_bound(target):
    left, right = 0, n - 1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if target < points[mid]:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

points.sort()

for x1, x2 in segments:
    lb = lower_bound(x1)
    ub = upper_bound(x2)
    if lb < ub:
        print(ub - lb)
    else:
        print(0)