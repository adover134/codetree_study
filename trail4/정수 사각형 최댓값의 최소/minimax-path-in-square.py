N = int(input())
grid = [list(map(int,input().split()))for _ in range(N)]

r, c = 0, 0
Map = [[0 for _ in range(N)] for _ in range(N)]
Map[0][0] = grid[0][0]
for i in range(1, N):
    Map[i][0] = max(grid[i][0], Map[i - 1][0])
for i in range(1, N):
    Map[0][i] = max(grid[0][i], Map[0][i - 1])
for i in range(1, N):
    for j in range(1, N):
        Map[i][j] = max(min(Map[i-1][j], Map[i][j-1]), grid[i][j])
print(Map[-1][-1])
