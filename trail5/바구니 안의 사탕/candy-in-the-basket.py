n, k = map(int, input().split())
MAX_POS = 1000000
candy = [0] * (MAX_POS + 1) # x 위치에 v개의 사탕 갯수 관리
for _ in range(n):
    c, p = map(int, input().split())
    candy[p] += c

# Please write your code here.
psum = [0] * (MAX_POS + 1)
psum[0] = candy[0]

for i in range(1, MAX_POS + 1):
    psum[i] = psum[i - 1] + candy[i]

answer = 0
for i in range(MAX_POS + 1):
    ei = i + (2 * k)
    if ei > MAX_POS:
        ei = MAX_POS
    answer = max(answer, psum[ei] - psum[i] + candy[i])
print(answer)
