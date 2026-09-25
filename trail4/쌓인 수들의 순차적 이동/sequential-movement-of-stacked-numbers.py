n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
move_nums = list(map(int, input().split()))

# Please write your code here.
pos = [0] * (n * n)
for r in range(n):
    for c in range(n):
        pos[grid[r][c] - 1] = (r, c)
        grid[r][c] = [grid[r][c]]

dr, dc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]

for mn in move_nums:
    r, c = pos[mn - 1]
    tr, tc, tmax = -1, -1, 0
    for d in range(8):
        ar, ac = r + dr[d], c + dc[d]
        if ar < 0 or ar >= n or ac < 0 or ac >= n:
            continue
        if grid[ar][ac]:
            amax = max(grid[ar][ac])
            if amax > tmax:
                tr, tc, tmax = ar, ac, amax
    if mn not in grid[r][c]:
        break
    if tmax == 0:
        continue
    p = grid[r][c].index(mn)
    for num in grid[r][c][p:]:
        pos[num-1] = (tr, tc)
    grid[tr][tc].extend(grid[r][c][p:])
    grid[r][c] = grid[r][c][:p]

for row in grid:
    for cell in row:
        if not cell:
            print(None)
        else:
            for num in reversed(cell):
                print(num, end = ' ')
            print()
