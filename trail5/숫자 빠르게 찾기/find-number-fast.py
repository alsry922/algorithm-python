n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
for query in queries:
    left, right = 0, n - 1
    pos = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == query:
            pos = mid + 1
            break
        if query > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print(pos)