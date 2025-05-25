import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dirY = [1, -1, 0, 0]
dirX = [0, 0, 1, -1]

def dfs(y, x):
    global graph, visited
    visited[y][x] = True
    
    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if not visited[newY][newX] and graph[newY][newX]:
            dfs(newY, newX)

# 0. 입력
T = int(input())

MAX = 50 + 10

while T:
    T -= 1
    M, N, K = map(int, input().split())
    
    graph = [[False]*MAX for _ in range(MAX)]
    visited = [[False]*MAX for _ in range(MAX)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y+1][x+1] = True
        
    # 1. dfs 호출
    answer = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1

    # 2. 출력
    print(answer)
    
