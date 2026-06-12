n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

j = 0
answer = 0
sum_val = arr[0]
for i in range(n):
    while j + 1 < n and sum_val + arr[j + 1] <= m:
        sum_val += arr[j + 1]
        j += 1
    
    if sum_val == m:
        answer += 1
    
    sum_val -= arr[i]

print(answer)