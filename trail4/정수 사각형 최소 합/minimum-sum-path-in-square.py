n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
for i in range(1, n):
    grid[i][n-1] += grid[i-1][n-1]
    grid[0][n-1-i] += grid[0][n-i]
for i in range(1, n):
    for j in range(1, n):
        t = n-1-j
        grid[i][t] += min(grid[i-1][t], grid[i][t+1])
print(grid[n-1][0])