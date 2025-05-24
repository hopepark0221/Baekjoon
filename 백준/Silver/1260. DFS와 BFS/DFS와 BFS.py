import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    visited[idx] = True
    print(idx, end = ' ')
    
    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)
            
def bfs():
    queue = []
    
    queue.append(V)
    visited[V] = True
    
    while queue:
        idx = queue.pop(0)
        print(idx, end = ' ')
        
        for i in range(1, N+1):
            if not visited[i] and graph[idx][i]:
                queue.append(i)
                visited[i] = True
            
# 0. 입력
N, M, V = map(int, input().split())
MAX = 1000 + 10
graph = [[False]*MAX for _ in range(MAX)]
visited = [False]*MAX

# 1. 그래프 연결
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
    
# 2. dfs 호출
dfs(V)
print()

# 3. bfs 호출
visited = [False]*MAX
bfs()