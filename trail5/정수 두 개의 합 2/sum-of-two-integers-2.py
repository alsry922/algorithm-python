n, k = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()
j = n
count = 0
for i in range(1, n + 1):
    while j > i and arr[i] + arr[j] > k:
        j -= 1

    if i >= j:
        break
    
    count += (j - i)

print(count)