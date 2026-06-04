from bisect import bisect_left, bisect_right
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()
# print(arr)
count = 0
for i in range(n):
    a = arr[i]
    b = k - arr[i]
    r_idx = bisect_right(arr, b) - 1
    # print(i, a, b, r_idx)
    if r_idx > 0 and r_idx > i:
        count += (r_idx - i)

print(count)