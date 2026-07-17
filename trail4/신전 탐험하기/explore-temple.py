n = int(input())
l, m, r = [0], [0], [0]
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)
MIN = float('-inf')
ROOM_CNT = 3
# Please write your code here.
# 최적화형 -> 여러 선택지 중 최선을 선택
# 연속성 -> 있음. 이전 층에서 선택한 방은 현재 층에서 선택 못함
# dp = i번째 층에서 j번 방을 들어갔을 때 얻을 수 있는 최대 보물 갯수
dp = [[MIN] * (ROOM_CNT + 1) for _ in range(n + 1)]
# 0층에서는 아무것도 못 얻음
dp[0][0] = 0
dp[1][1] = l[1]
dp[1][2] = m[1]
dp[1][3] = r[1]

for i in range(2, n + 1):
    for j in range(1, ROOM_CNT + 1):
        if j == 1:
            jewel = l[i]
        elif j == 2:
            jewel = m[i]
        else:
            jewel = r[i]

        for k in range(1, ROOM_CNT + 1):
            # 이전 층이랑 같은 방 못 들어감
            if j == k:
                continue
            # if k == 1:
            #     prev_jewel = l[i]
            # elif k == 2:
            #     prev_jewel = m[i]
            # else:
            #     prev_jewel = r[i]
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + jewel)

print(max(dp[n]))
            