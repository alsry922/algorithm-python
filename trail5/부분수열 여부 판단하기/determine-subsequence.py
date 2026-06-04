n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

# Please write your code here.

is_subsequence = True
i = 1
for j in range(1, m + 1):
    while i <= n and A[i] != B[j]:
        i += 1
    
    if i == n + 1:
        is_subsequence = False
        break

if is_subsequence:
    print('Yes')
else:
    print('No')