s = int(input())

# Please write your code here.
left, right = 1, 10 ** 18
answer = 0
while left <= right:
    mid = (left + right) // 2
    sum_val = mid * (mid + 1) // 2
    if sum_val <= s:
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)