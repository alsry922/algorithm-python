# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

ans = 0

# 구간을 잡아봅니다.
sum_val = 0
j = 0
for i in range(1, n + 1):
    # 구간 내 합이 m보다 작으면 계속 진행합니다.
    while j + 1 <= n and sum_val < m:
        sum_val += arr[j + 1]
        j += 1

    # 구간 내 합이 m이 되면 정답을 1 증가시킵니다.
    if sum_val == m:
        ans += 1

    # 다음 구간으로 넘어가기 전에
    # arr[i]에 해당하는 값은 구간에서 제외시킵니다.
    sum_val -= arr[i]

# 정답을 출력합니다.
print(ans)
