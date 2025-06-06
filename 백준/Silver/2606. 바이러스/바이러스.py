import sys
input = sys.stdin.readline

def dfs(idx):
    global map_, visited, N, answer
    
    visited[idx] = True
    answer += 1
    
    for i in range(1, N+1):
        if not visited[i] and map_[idx][i]:
            dfs(i)
            
# 0. 입력
N = int(input())
M = int(input())
map_ = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
answer = 0

# 1. map 채우기
for _ in range(M):
    x, y = map(int, input().split())
    map_[x][y] = True
    map_[y][x] = True
    
# 2. dfs 호출
dfs(1)

# 3. answer 출력
print(answer-1)