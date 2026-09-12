n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
nums = sorted((grid[i][j], i, j) for i in range(n) for j in range(n))
dx, dy = [1,-1,0,0],[0,0,1,-1]
Map = [[0 for _ in range(n)] for _ in range(n)]
maxi = 0
for v, x, y in nums:
    m = 0
    for d in range(4):
        ax, ay = x+dx[d], y+dy[d]
        if ax<0 or ax==n or ay<0 or ay==n:
            continue
        if grid[ax][ay]<grid[x][y]:
            m = max(Map[ax][ay], m)
    Map[x][y] = m+1
    maxi = max(Map[x][y], maxi)
print(maxi)