n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.

sum_val = 0
j = 0
count = 0
for i in range(1, n + 1):
    while j + 1 <= n and sum_val < m:
        # print(f'i={i}, j+1={j+1}, , sum_val={sum_val}, arr[{i}]={arr[i]}, arr[j + 1]={arr[j + 1]}')
        sum_val += arr[j + 1]
        j += 1

    # if j + 1 > n:
        # break
    
    if sum_val == m:
        count += 1
    
    sum_val -= arr[i]

print(count)
