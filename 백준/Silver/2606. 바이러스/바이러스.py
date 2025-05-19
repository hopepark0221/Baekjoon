def dfs(idx):
    global answer, graph, visited
    visited[idx] = True
    answer += 1
    
    for i in range(N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

# 0. 입력
N = int(input())
M = int(input())
graph = [[False]*(N+1) for _ in range(N+1)]
visited = [False] * (N+1)
answer = 0

# 1. 그래프
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
    
# 2. 호출
dfs(1)

# 3. 출력
print(answer - 1)