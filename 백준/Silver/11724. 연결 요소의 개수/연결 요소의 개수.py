import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx):
    global graph, visited
    
    visited[idx] = True
    
    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

# 0. 입력
N, M = map(int, input().split())
MAX = 1000 + 10
answer = 0
graph = [[False]*MAX for _ in range(MAX)]
visited = [False] * MAX

# 1. 그래프 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
    
# 2. dfs 불러오기
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        answer += 1
        
# 3. 출력
print(answer)