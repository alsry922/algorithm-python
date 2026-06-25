n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

def binary_search(query):
    left, right = 0, n - 1
    idx = -1
    while left <= right:
        mid = (left + right) // 2
        if query == arr[mid]:
            idx = mid

        if query < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return idx
# Please write your code here.
for query in queries:
    idx = binary_search(query)
    print(-1 if idx == -1 else idx + 1)
        