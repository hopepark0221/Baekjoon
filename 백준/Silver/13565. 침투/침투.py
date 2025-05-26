import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dirY = [-1, 1, 0, 0]
dirX = [0, 0, -1, 1]

def dfs(y, x):
    global visited, map_, answer, M
    
    if y == M:
        answer = True
        return
    
    visited[y][x] = True
    
    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        
        if not visited[newY][newX] and map_[newY][newX]:
            dfs(newY, newX)

# 0. 입력
M, N = map(int, input().split())
MAX = 1000 + 10
map_ = [[False]*MAX for _ in range(MAX)]
visited = [[False]*MAX for _ in range(MAX)]

# 1. map 연결
for i in range(1, M+1):
    row = input()
    for j in range(1, N+1):
        map_[i][j] = (row[j-1] == "0")
        
# 2. dfs 호출
answer = False
for j in range(1, N+1):
    if map_[1][j]:
        dfs(1, j)
        
# 3. 출력
print("YES" if answer else "NO")