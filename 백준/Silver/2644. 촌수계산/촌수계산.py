import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())

def dfs(index, count):
    global visited, graph, answer, end
    visited[index] = True
    if index == end:
        answer = count
        return
    for i in range(1, n+1):
        if graph[index][i] and not visited[i]:
            dfs(i, count+1)

visited = [False] * (n+1)
graph = [[False]* (n+1) for _ in range(n+1)]
answer = -1

for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

dfs(start, 0)
print(answer)
