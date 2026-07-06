n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
# 한 번에 생각하려니까 어려워. 따로 나눠서 생각해보자.
# 우선 증가하는 부분 수열을 생각해보자.
# dp[i] = i번째 원소까지 고려했을 때 만들 수 있는 증가 부분 수열의 최대 길이
#   초기값은 1로 설정. i번째 수가 어떤 수든 i번째 수 하나는 무조건 뽑을 수 있음.
#   i번째가 i-1번째 원소들 중 가장 큰 수인 경우 뽑을 수 있음. dp[i] = max(dp[i], dp[i-1] + 1)
# 감소하는 부분 수열도 마찬가지.
# 그럼 가장 긴 증가-감소 부분 수열은 어떻게 하지? 이게 문제네.
# LR 테크닉을 쓰면 되려나? (직감적으로 생각이 들었음.)
# L = 왼쪽부터 살펴보면서 가장 큰 수를 기록
# R = 오른족부터 살펴보면서 가장 큰 수를 기록
# dp를 LR로 해보자. 
#   ldp = 왼쪽에서부터 증가부분수열 길이
#   rdp = 오른쪽에서부터 증가부분수열 길이.
#   지금 살펴보는 i번째 위치를 기준으로 ldp[i] + rdp[i] - 1을 하면 증가-감소 부분수열 길이를 구할 수 있을 것 같은데?
# 그럼 다시 정리해보자.
# inc_dp[i] = i번째 원소까지 고려했을 때 증가 부분 수열의 최대 길이
# dec_dp[i] = i번째 원소까지 고려했을 때 감소 부분 수열의 최대 길이
# inc_dec_dp[i] = i번재 원소를 기준으로 증가-감소 부분 수열을 만들 때 최대 길이
# dp[i] = i번째 원소까지 고려했을 때 만들 수 있는 증가 부분 수열의 최대 길이
#   근데 이렇게 하면 dp의 정의가 inc_dp, dec_dp는 index를 맞춰서 할 수 있는데 inc_dec_dp랑은 불가능 한 거 아닌가?
#   정의상 inc_dec_dp는 처음부터 끝까지 모든 원소를 살펴본 경우에 해당하는데... 흠...
#   아 inc_dec_dp[i]도 i 번째 원소까지 고려했을 때의 증가-감소 부분 수열로 하고, 매번 ldp, rdp를 구해서 계산하면 될 것 같은데?
# inc_dp 정의하는데 O(N)
# dec_dp 정의하는데 O(N)
# inc_dec_dp 정의하려면 i를 증가시키며 i번째까지 고려할 때마다 i길이 만큼 매번 살펴보여 ldp, rdp를 정의해야하니까 O(N^2)
# 따라서 최종 시간복잡도는 O(N^2)이고 제한조건을 만족하겠는데?
# 아니, 다 할 필요가 없네.
# inc_dec_dp를 구하면 증가 부분 수열, 감소 부분 수열, 증가-감소 부분 수열 모든게 커버된데

dp = [1] * n
L = [1] * n
R = [1] * n
for i in range(1, n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            L[i] = max(L[i], L[j] + 1)
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if sequence[i] > sequence[j]:
            R[i] = max(R[i], R[j] + 1)

for i in range(n):
    dp[i] = max(dp[i], L[i] + R[i] - 1)

print(max(dp))