n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
from collections import deque
area = set()
r, c = r - 1, c - 1
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
for i in range(grid[r][c]):
    for d in range(4):
        ar, ac = r + dr[d] * i, c + dc[d] * i
        if ar < 0 or ar >= n or ac < 0 or ac >= n:
            continue
        grid[ar][ac] = 0

for i in range(1, n):
    for j in range(n):
        if grid[i][j] == 0:
            for k in range(i):
                grid[i-k][j] = grid[i-k-1][j]
                grid[i-k-1][j] = 0

for g in grid:
    for num in g:
        print(num, end = ' ')
    print()