A = input()

# Please write your code here.

two_close = [0] * len(A)

for i in range(len(A) - 2, -1, -1):
    two_close[i] = two_close[i + 1]
    if A[i] == ')' and A[i + 1] == ')':
        two_close[i] += 1
answer = 0
for i in range(1, len(A) - 1):
    if A[i] == '(' and A[i - 1] == '(':
        answer += two_close[i + 1]
    
print(answer)