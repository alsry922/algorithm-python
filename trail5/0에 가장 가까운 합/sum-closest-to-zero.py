import sys
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()
j = n - 1
answer = sys.maxsize

for i in range(n):
    while i < j and a[i] + a[j] > 0:
        answer = min(answer, abs(a[i] + a[j]))
        j -= 1
    if i >= j:
        break
    answer = min(answer, abs(a[i] + a[j]))
    
print(answer)