n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
MAX_NUM = max(arr)
counting = [0] * (MAX_NUM + 1)
answer = 0
j = 0
for i in range(1, n + 1):
    while j + 1 <= n and counting[arr[j + 1]] < 1:
        counting[arr[j + 1]] += 1
        j += 1
    
    answer = max(answer, j - i + 1)

    counting[arr[i]] -= 1

print(answer)