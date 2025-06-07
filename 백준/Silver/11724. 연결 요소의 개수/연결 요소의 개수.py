import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx):
    global map_, visited
    
    visited[idx] = True
    
    for i in range(1, N+1):
        if not visited[i] and map_[idx][i]:
            dfs(i)

# 0. 입력
N, M = map(int, input().split())
map_ = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)
answer = 0

# 1. 채우기
for _ in range(M):
    x, y = map(int, input().split())
    map_[x][y] = True
    map_[y][x] = True
    
# 2. dfs 출력
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        answer += 1

# 3. 답변 출력
print(answer)