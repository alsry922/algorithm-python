n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
sum_val = 0
j = 0
MAX_RANGE = 100000
answer = MAX_RANGE
for i in range(1, n + 1):
    while j + 1 <= n and sum_val + arr[j + 1] < s:
        sum_val += arr[j + 1]
        j += 1
    
    if j + 1 > n:
        break
    
    answer = min(answer, j + 2 - i)

    sum_val -= arr[i]

print(answer if answer != MAX_RANGE else -1)