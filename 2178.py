from collections import deque
import sys

N, M = map(int, input().split())  
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]  

dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]  

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    return graph[N-1][M-1]

print(bfs(0, 0))


# 아래는 visited 사용(원본(graph)을 수정하지 않음)
# 딴 사람이 푼 코드 
from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, list(input().strip()))) for _ in range(N)]

q = deque([(0, 0, 1)])
visited = [[False] * M for _ in range(N)]
visited[0][0] = True

# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y, z = q.popleft()
    
    if x == N - 1 and y == M - 1:
        print(z)
        break
    
    for i in range(4):  # 4방향 탐색 (대각선 제외)
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny, z + 1))
