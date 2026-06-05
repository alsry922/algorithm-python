n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
j = 0
is_subsequence = True
for i in range(m):
    while j < n and A[j] != B[i]:
        j += 1
    
    # 다 살펴보았는데 조건을 만족하지 못해서 while 문을 빠져나옴
    if j == n:
        is_subsequence = False
        break
    
    if A[j] == B[i]:
        j += 1


if is_subsequence:
    print('Yes')
else:
    print('No')
