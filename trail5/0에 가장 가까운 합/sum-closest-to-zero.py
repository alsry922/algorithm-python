n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
# 정렬
a.sort()
# i는 증가, j는 감소시켜야 함.
j = n - 1
answer = float('inf')
for i in range(n):
    while i < j and a[i] + a[j] > 0:
        answer = min(answer, abs(a[i] + a[j]))
        j -= 1

    if i >= j:
        break
    
    answer = min(answer, abs(a[i] + a[j]))

print(answer)