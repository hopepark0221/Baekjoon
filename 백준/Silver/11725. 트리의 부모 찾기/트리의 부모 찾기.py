import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx):
    global visited, answer, graph
    visited[idx] = True
    
    for next in graph[idx]:
        
        if not visited[next]:
            answer[next] = idx
            dfs(next)

# 1. 입력
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
answer = [0]*(N+1)

# 2. 그래프 채우기
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
# 3. dfs 호출
dfs(1)

# 4. 답 출력
for i in range(2, N+1):
    print(answer[i])