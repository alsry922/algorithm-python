n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
def lower_bound(target):
    l, r = 0, n - 1
    min_idx = n
    while l <= r:
        mid = (l + r) // 2
        if target <= arr[mid]:
            min_idx = min(min_idx, mid)
            r = mid - 1
        else:
            l = mid + 1
    return min_idx

def upper_bound(target):
    l, r = 0, n - 1
    min_idx = n
    while l <= r:
        mid = (l + r) // 2
        if target < arr[mid]:
            min_idx = min(min_idx, mid)
            r = mid - 1
        else:
            l = mid + 1
    return min_idx

for query in queries:
    lb = lower_bound(query)
    rb = upper_bound(query)
    print(rb - lb)