n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

# Please write your code here.
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
for M in range(m):
    c = commands[M] - 1
    f = False
    for r in range(n):
        if grid[r][c] > 0:
            f = True
            break
    if not f:
        continue
    for i in range(grid[r][c]):
        for d in range(4):
            ar, ac = r + dr[d] * i, c + dc[d] * i
            if ar < 0 or ar >= n or ac < 0 or ac >= n:
                continue
            grid[ar][ac] = 0
    for row in range(1, n):
        for c in range(n):
            if grid[row][c] == 0:
                k = row
                while k > 0:
                    grid[k][c] = grid[k - 1][c]
                    grid[k - 1][c] = 0
                    k -= 1

for g in grid:
    for num in g:
        print(num, end = ' ')
    print()