n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
j = 0
is_subsequence = True
for i in range(m):
    while j < n and A[j] != B[i]:
        j += 1
    
    if j == n:
        is_subsequence = False
        break
    
print('Yes' if is_subsequence else 'No')