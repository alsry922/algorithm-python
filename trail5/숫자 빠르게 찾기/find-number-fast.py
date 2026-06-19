n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
for query in queries:
    l, r = 0, n - 1
    pos = n
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == query:
           pos = mid
           break
        if query < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    if pos == n:
        print(-1)
    else:
        print(pos + 1)