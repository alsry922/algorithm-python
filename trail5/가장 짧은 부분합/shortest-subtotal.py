n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
psum = [0] * (n + 1)
for i in range(1, n + 1):
    psum[i] = psum[i - 1] + arr[i]

# print(psum)
j = 0
answer = 100000
for i in range(n + 1):
    # 인덱스를 초과하지 않고 합이 S 미만인 경우까지 반복
    while j + 1 <= n and psum[j + 1] - psum[i] < s:
        j += 1
    if j + 1 <= n:
        answer = min(answer, j + 1 - i)

    # print(i, j + 1, answer)
print(answer if answer != 100000 else -1)