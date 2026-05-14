import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

S = sum(arr)
if S % 4 != 0:
    print(0)
else:
    prefix = [0] * (n + 1)
    suffix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + arr[i-1]
    for i in range(n-1, -1, -1):
        suffix[i] = suffix[i+1] + arr[i]

    t = S // 4
    lcnt = 0
    rcnt = sum(1 for i in range(1, n) if suffix[i] == t)
    ans = 0

    for j in range(1, n):
        if suffix[j] == t:
            rcnt -= 1
        if prefix[j] == 2 * t:
            ans += lcnt * rcnt
        if prefix[j] == t:
            lcnt += 1

    print(ans)