# import sys

# sys.stdin = open("sample.txt", "r")

T = int(input())
# T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    grid = [[0]*10 for _ in range(10)] # 격자
    color = [1, 2, 3] # 빨강, 파랑, 보라

    area = int(input())
    # area = int(sys.stdin.readline())
    overPainted = 0 # 덧칠된 위치의 갯수

    for i in range(area):
        paintInfo = list(map(int, input().split()))
        # paintInfo = list(map(int, sys.stdin.readline().split()))

        color = paintInfo[4]
        for j in range(paintInfo[0], paintInfo[2]+1): # 행
            for k in range(paintInfo[1], paintInfo[3]+1): # 열
                if grid[j][k] == 0:
                    grid[j][k] = color
                else:
                    grid[j][k] = 2
                    overPainted += 1
    print(f'#{test_case} {overPainted}')


