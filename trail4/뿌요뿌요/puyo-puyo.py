# 변수 선언 및 입력:
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

max_block, bomb_cnt = 0, 0
curr_block_num = 0


# 탐색하는 위치가 격자 범위 내에 있는지 여부를 반환합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 탐색하는 위치로 움직일 수 있는지 여부를 반환합니다.
def can_go(x, y, color):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] != color:
        return False
    
    return True
    

def dfs(x, y):
    global curr_block_num
    
    #0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    # 네 방향 각각에 대하여 DFS 탐색을 합니다.
    for dx, dy, in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if can_go(new_x, new_y, grid[x][y]):
            visited[new_x][new_y] = True
            # 블럭이 하나 추가됩니다.
            curr_block_num += 1
            dfs(new_x, new_y)

            
# 격자의 각 위치에서 탐색을 시작할 수 있는 경우
# 한 블럭에 대한 DFS 탐색을 수행합니다.
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            # 해당 블럭을 방문할 수 있는 경우 visited 배열을 갱신하고
            # 새로운 블럭을 탐색한다는 의미로 curr_block_num을 1으로 갱신합니다.
            visited[i][j] = True
            curr_block_num = 1
            
            dfs(i, j)
            
            # 한 블럭 묶음에 대한 탐색이 끝난 경우 답을 갱신합니다.
            if curr_block_num >= 4:
                bomb_cnt += 1
                
            max_block = max(max_block, curr_block_num)

print(bomb_cnt, max_block)
