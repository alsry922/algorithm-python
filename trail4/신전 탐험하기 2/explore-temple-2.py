n = int(input())
l, m, r = [], [], []
room = [(0, 0, 0)]
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)
    room.append((left, mid, right))
MIN = float('-inf')
ROOM_CNT = 3
# Please write your code here.
# dp = i번째 층에서 j번 방에 들어갔고, 1층에서 k번 방에 들어갔을 때, 얻을 수 있는 최대 보물 갯수
dp = [[[MIN] * (ROOM_CNT) for _ in range(ROOM_CNT)] for _ in range(n + 1)]
dp[1][0][0] = room[1][0]
dp[1][1][1] = room[1][1]
dp[1][2][2] = room[1][2]
for i in range(2, n + 1):
    for first in range(ROOM_CNT):
        for j in range(ROOM_CNT):
            for k in range(ROOM_CNT):
                # 이전 층과 같은 방은 안됨.
                if j == k:
                    continue
                if i == n and j == first:
                    continue
                dp[i][j][first] = max(dp[i][j][first], dp[i - 1][k][first] + room[i][j])

answer = 0
for i in range(ROOM_CNT):
    for j in range(ROOM_CNT):
        answer = max(answer, dp[n][i][j])
print(answer)