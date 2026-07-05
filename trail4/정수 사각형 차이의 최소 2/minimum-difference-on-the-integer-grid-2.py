n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 문제를 보면 격자에서의 bfs 같지만, 이동 방향이 정해져 있음. 사이클이 생성될 수 없음. dp로 해결 가능
# dp[i][j] = (1, 1)에서 시작하여 (i, j)까지 이동했을 때 거쳐간 위치에서 적혀있는 수들 중 최댓값과 최솟값의 차이가 가장 작은 값.
# dp 하나로 상태가 정의되지 않을 것 같다.(상태 분리 문제인 듯)
#   1. (1, 1)에서 (i, j)까지 이동했을 때 최댓값 중 최솟값을 정의하는 상태 = min_of_max
#   2. (1, 1)에서 (i, j)까지 이동했을 때 최솟값 중 최댓값을 정의하는 상태 = max_of_min
#   dp[i][j] 에는 이 두 상태의 차를 기록해야 함.
# 시간복잡도
#   min_of_max를 구성하는데 O(N^2)
#   max_of_min을 구성하는데 O(N^2)
#   dp를 채우는데 O(N^2)
#   따라서, 최종 시간복잡도는 O(N^2)

# 위 상태 정의는 잘못됐음. 하나의 이동 루트에서의 최대 - 최소가 가장 작은 값을 기록해야함.
# 즉, "dp[i][j] = (1, 1) ~ (i, j)까지 이동했을 때 거쳐온 수들 중 최댓값과 최솟값의 차이가 가장 작은 수" 이렇게 됨.
# 그럼 dfs를 통해 이동 루트의 값들을 기록하고 각각 계산?
#   dfs의 이동 경로 가짓수 (2N - 2) ^ 2 정도 됨. -> 시작 위치와 종료위치를 제외하고 각각 위치에서 두 가지 방향으로 나아갈 수 있으니까
#   이동을 완료할 때마다 이동 경로 값을 기록한 2N - 1 길이 배열에서 min, max값 가지고 차이를 계산해야 하니까 O(2N - 1)만큼의 시간이 걸림
#   최종시간복잡도는 결국 O(N ^ 3)으로 시간복잡도를 가지는데 1억을 넘지 않으므로 가능할 것 같음
#   이동 경로 갯수 계산이 잘못됨. 이항계수(조합식으로)
#       R -> N - 1, D -> N - 1번 이동해야 끝 점으로 갈 수 있음.
#       전체 이동 2N - 2 번의 이동을 R,D,R,D... 순으로 나열한 것.
#       결국 경로의 갯수는 "2N - 2개의 자리 중에서 D가 들어갈 자리 N - 1개를 고르는 경우의 수가 됨."
#       (2N - 2)! / (N - 1)!*(2N - 2 - N + 1)!

# m(최솟값)이 될 수 있는 범위는 1 ~ 100
# dp[i][j][m] = (1, 1) ~ (i, j)까지 이동했을 때 최솟값의 m 일 때의 최댓값의 최솟값.
dp = [
    [[101 for _ in range(101)] for _ in range(n)] for _ in range(n)
]

def init():
    dp[0][0][grid[0][0]] = grid[0][0]
    for j in range(1, n):
        v = grid[0][j]
        for m_prime in range(101):
            if dp[0][j-1][m_prime] == 101:
                continue # 기록 없음, 건너뜀
            new_m = min(m_prime, v)
            new_max = max(dp[0][j-1][m_prime], v)
            dp[0][j][new_m] = min(dp[0][j][new_m], new_max)
    
    for i in range(1, n):
        v = grid[i][0]
        for m_prime in range(101):
            if dp[i-1][0][m_prime] == 101:
                continue # 기록 없음, 건너뜀
            new_m = min(m_prime, v)
            new_max = max(dp[i-1][0][m_prime], v)
            dp[i][0][new_m] = min(dp[i][0][new_m], new_max)

init()
for i in range(1, n):
    for j in range(1, n):
        v = grid[i][j]
        for m_prime in range(101):
            new_m = min(m_prime, v)
            if dp[i-1][j][m_prime] != 101:
                new_max = max(dp[i-1][j][m_prime], v)
                dp[i][j][new_m] = min(dp[i][j][new_m], new_max)
            if dp[i][j-1][m_prime] != 101:
                new_max = max(dp[i][j-1][m_prime], v)
                dp[i][j][new_m] = min(dp[i][j][new_m], new_max)

answer = 101
for m in range(1, 101):
    if dp[n-1][n-1][m] == 101:
        continue
    answer = min(answer, dp[n-1][n-1][m] - m)

print(answer)