import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y, x):
    global visited, map_
    
    visited[y][x] = True
    
    if map_[y][x] == '-' and map_[y][x+1] == '-':
        dfs(y, x+1)
    elif map_[y][x] == '|' and map_[y+1][x] == '|':
        dfs(y+1, x)
    
# 0. 입력
MAX = 50 + 10
N, M = map(int, input().split())
visited = [[False]*MAX for _ in range(MAX)]
map_ = [['']*MAX for _ in range(MAX)]

# 1. map 연결
for i in range(1, N+1):
    line = input()
    for j in range(1, M+1):
        map_[i][j] = line[j-1]
        
# 2. dfs 호출
answer = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if not visited[i][j]:
            dfs(i, j)
            answer += 1
        
# 3. answer 출력
print(answer)