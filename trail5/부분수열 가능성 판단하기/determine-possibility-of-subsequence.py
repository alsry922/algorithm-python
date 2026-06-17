n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
L = [0] * (m)
R = [0] * (m)

j = 0
for i in range(m):
    while j <= n - 1 and A[j] != B[i]:
        j += 1
    L[i] = j
    j += 1

j = n - 1
for i in range(m - 1, -1, -1):
    while j >= 0 and A[j] != B[i]:
        j -= 1
    R[i] = j
    j -= 1

L = [-1] + L
R = R + [n]
count = 0
for k in range(m):
    if L[k] < R[k+1]:
        count += 1

print(count)