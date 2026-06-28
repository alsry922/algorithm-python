n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

def is_possible(x):
    count = 0
    for num in arr:
        count += num // x
    
    return count >= m

left, right = 1, 100000
answer = 0
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)