# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
if dir == 'L':
    for r in range(4):
        a = []
        t = False
        for c in range(4):
            if grid[r][c] == 0:
                continue
            elif a and a[-1] == grid[r][c] and t:
                a[-1] *= 2
                t = False
            else:
                a.append(grid[r][c])
                t = True
        for i in range(len(a), 4):
            a.append(0)
        grid[r] = a
if dir == 'R':
    for r in range(4):
        a = []
        t = False
        for c in range(3, -1, -1):
            if grid[r][c] == 0:
                continue
            elif a and a[-1] == grid[r][c] and t:
                a[-1] *= 2
                t = False
            else:
                a.append(grid[r][c])
                t = True
        for i in range(len(a), 4):
            a.append(0)
        grid[r] = a[::-1]
if dir == 'U':
    for c in range(4):
        a = []
        t = False
        for r in range(4):
            if grid[r][c] == 0:
                continue
            elif a and a[-1] == grid[r][c] and t:
                a[-1] *= 2
                t = False
            else:
                a.append(grid[r][c])
                t = True
        for i in range(len(a), 4):
            a.append(0)
        for r in range(4):
            grid[r][c] = a[r]
if dir == 'D':
    for c in range(4):
        a = []
        t = False
        for r in range(3, -1, -1):
            if grid[r][c] == 0:
                continue
            elif a and a[-1] == grid[r][c] and t:
                a[-1] *= 2
                t = False
            else:
                a.append(grid[r][c])
                t = True
        for i in range(len(a), 4):
            a.append(0)
        for r in range(4):
            grid[r][c] = a[3-r]

for g in grid:
    for num in g:
        print(num, end=' ')
    print()