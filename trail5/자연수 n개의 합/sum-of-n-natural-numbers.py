s = int(input())

# Please write your code here.
left, right = 1, 10 ** 18
answer = 0
while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= s:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)