N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
from collections import deque

visited = [[False for _ in range(N)] for _ in range(N)]
res = [[0 for _ in range(N)] for _ in range(N)]

dq = deque([])

for r in range(N):
    for c in range(N):
        if grid[r][c] == 0:
            visited[r][c] = True
            res[r][c] = -1
        elif grid[r][c] == 2:
            dq.append((r,c))
            visited[r][c] = True

dx, dy = [0,0,1,-1], [1,-1,0,0]

while dq:
    x, y = dq.popleft()
    for d in range(4):
        ax, ay = x+dx[d], y+dy[d]
        if ax < 0 or ax >= N or ay < 0 or ay >=N:
            continue
        if grid[ax][ay] != 1:
            continue
        if visited[ax][ay]:
            continue
        res[ax][ay] = res[x][y] + 1
        visited[ax][ay] = True
        dq.append((ax, ay))
for r in range(N):
    for c in range(N):
        if visited[r][c] == False:
            print(-2, end = ' ')
        else:
            print(res[r][c], end = ' ')
    print()
        