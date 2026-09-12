n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 주위 4칸이 모두 자신보다 작다면
# 모두 시작 칸으로 지정한다.
Map = [[0 for _ in range(n)] for _ in range(n)]
from collections import deque
dq = deque()
dx, dy = [0,0,1,-1], [1,-1,0,0]
for r in range(n):
    for c in range(n):
        f = False
        for d in range(4):
            ax, ay = r+dx[d], c+dy[d]
            if ax<0 or ax==n or ay<0 or ay==n:
                continue
            if grid[ax][ay] < grid[r][c]:
                f = True
                break
        if not f:
            dq.append((r, c))
            Map[r][c] = 1
while dq:
    x, y = dq.popleft()
    for d in range(4):
        ax, ay = x+dx[d], y+dy[d]
        if ax<0 or ax==n or ay<0 or ay==n:
            continue
        if grid[ax][ay] <= grid[x][y]:
            continue
        if Map[ax][ay]<(Map[x][y]+1):
            f = False
            t = False
            maxi = 0
            for i in range(4):
                aax, aay = ax+dx[i], ay+dy[i]
                if aax<0 or aax==n or aay<0 or aay==n:
                    continue
                if grid[ax][ay]>grid[aax][aay]:
                    t = True
                    if Map[aax][aay] == 0:
                        f = True
                        break
                    else:
                        maxi = max(maxi, Map[aax][aay])
            if not f and t:
                dq.append((ax, ay))
                Map[ax][ay]=maxi+1
print(max(max(m) for m in Map))