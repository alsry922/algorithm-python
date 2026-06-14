from collections import defaultdict
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
count = defaultdict(int)
j = 0

answer = 1
for i in range(1, n + 1):
    while j + 1 <= n and count[arr[j + 1]] < k:
        count[arr[j + 1]] += 1
        j += 1
    
    answer = max(answer, j - i + 1)

    count[arr[i]] -= 1

print(answer)