import bisect
n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def custom_bound(target):
    left, right = 0, n - 1
    max_idx = -1
    while left <= right:
        mid = (left + right) // 2
        if points[mid] <= target:
            max_idx = max(max_idx, mid)
            left = mid + 1
        else:
            right = mid - 1
    
    return max_idx
points.sort()
for x1, x2 in segments:
    lb = bisect.bisect_left(points, x1)
    rb = custom_bound(x2)
    if lb > rb:
        print(0)
    else:
        print(rb - lb + 1)
