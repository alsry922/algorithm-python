n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
MAX_NUM = max(arr)
count_arr = [0] * (MAX_NUM + 1)
j = 0
answer = 0
for i in range(1, n + 1):
    while j + 1 <= n and count_arr[arr[j + 1]] < 1:
        count_arr[arr[j + 1]] += 1
        j += 1
    
    answer = max(answer, j - i + 1)

    count_arr[arr[i]] -= 1

print(answer)
