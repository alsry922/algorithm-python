n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
def lower_bound(target, left, right):
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if query <= arr[mid]:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

def upper_bound(target, left, right):
    min_idx = n
    while left <= right:
        mid = (left + right) // 2
        if query < arr[mid]:
            min_idx = min(min_idx, mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx

for query in queries:
    left, right = 0, n - 1
    lb = lower_bound(query, left, right)
    ub = upper_bound(query, left, right)
    print(ub - lb)
    