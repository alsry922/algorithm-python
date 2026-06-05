from bisect import bisect_left, bisect_right
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()
i, j = 0, n-1
count = 0

for i in range(n):
    while j >= 0 and arr[i] + arr[j] > k:
        j -= 1
    
    if j < 0 or i >= j:
        break
    
    count += (j - i)

print(count)
