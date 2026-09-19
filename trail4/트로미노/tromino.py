n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 가능한 각 모양마다
# 이동하면서
# 합을 구해본다.
# [i][j]+[i+1][j:j+2]
# [i][j+1]+[i+1][j:j+2]
# [i][j:j+2]+[i+1][j]
# [i][j:j+2]+[i+1][j+1]

# [i][j:j+3]
# [i:i+3][j]

a = 0
for i in range(n-1):
    for j in range(m-1):
        a = max([grid[i][j]+sum(grid[i+1][j:j+2]),
        grid[i][j+1]+sum(grid[i+1][j:j+2]),
        sum(grid[i][j:j+2])+grid[i+1][j],
        sum(grid[i][j:j+2])+grid[i+1][j+1], a])
for g in grid:
    t = max(sum(g[j:j+3]) for j in range(m-2))
    a = max(a, t)
for g in zip(*grid):
    t = max(sum(g[j:j+3]) for j in range(n-2))
    a = max(a, t)
print(a)