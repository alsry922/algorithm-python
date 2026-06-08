n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()
j = n - 1
answer = 0
for i in range(n):
    while j >= 0 and arr[i] + arr[j] > k:
        j -= 1
    
    if i >= j:
        break
    
    answer += (j - i)

print(answer)