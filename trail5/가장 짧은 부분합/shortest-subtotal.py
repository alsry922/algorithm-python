n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

MAX_LENGTH = 100000
sum_val = 0 # 지금까지의 합
j = 0 # 다음 뽑을 인덱스
answer = MAX_LENGTH
for i in range(n):
    while j < n and sum_val < s:
        sum_val += arr[j]
        j += 1
    
    if sum_val < s:
        break
    
    answer = min(answer, j - i)

    sum_val -= arr[i]

print(-1 if answer == MAX_LENGTH else answer)