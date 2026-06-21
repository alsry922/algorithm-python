s = int(input())

# Please write your code here.
# 후보값 x([1, x]) 가 커질수록 합도 커짐.
# 후보값 x가 작아질수록 합도 작아짐.
# 단조성 확인

# n(n + 1) <= 2s
# n^2 <= 2s
# n^2 <= 2 * 10^18
# n <= 2 * 10 ^ 9

left, right = 1, 2 * 10 ** 9
answer = 0
while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= s:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)