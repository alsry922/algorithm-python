n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.

MAX_LENGTH = 100000
sum_val = 0 # 지금까지의 합
j = 0 
answer = MAX_LENGTH
for i in range(1, n + 1):
    while j + 1 <= n and sum_val < s:
        sum_val += arr[j + 1]
        j += 1

    if sum_val < s:
        break

    answer = min(answer, j - i + 1)

    sum_val -= arr[i]

print(-1 if answer == MAX_LENGTH else answer)