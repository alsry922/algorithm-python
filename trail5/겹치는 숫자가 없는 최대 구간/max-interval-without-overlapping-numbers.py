n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
MAX_DUP = 1
MAX_NUM = max(arr)
count = [0] * (MAX_NUM + 1)

j = 0
answer = 0
for i in range(1, n + 1):
    while j + 1 <= n and count[arr[j + 1]] != MAX_DUP:
        count[arr[j + 1]] += 1
        j += 1
    
    answer = max(answer, j - i + 1)

    count[arr[i]] -= 1

print(answer)
