n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.
def lower_bound(target):
    left, right = 0, n - 1
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        # if target == arr[mid]:
        #     min_idx = min(min_idx, mid)
        if target <= arr[mid]:
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
        # if target == arr[mid]:
        #     min_idx = min(min_idx, mid)
        if target < arr[mid]:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

for target in query:
    lb = lower_bound(target)
    ub = upper_bound(target)
    print(-1 if lb == ub else lb + 1)