n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.
def lower_bound(target, left, right):
    min_idx = n + 1
    while left <= right:
        mid = (left + right) // 2
        if x <= arr[mid]:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

def upper_bound(target, left, right):
    min_idx = n + 1
    while left <= right:
        mid = (left + right) // 2
        if x < arr[mid]:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

for x in query:
    left, right = 1, n
    min_idx = n + 1
    lb = lower_bound(x, left, right)
    ub = upper_bound(x, left, right)
    if lb == ub:
        print(-1)
    else:
        print(lb)