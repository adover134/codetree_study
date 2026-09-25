n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 1부터 N*N까지 순서대로 위치를 list로 우선 저장한다.
points = [()] * (n * n)
for r in range(n):
    for c in range(n):
        points[grid[r][c]-1] =(r, c)
nums = n * n
dr, dc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
for _ in range(m):
    for num in range(nums):
        r, c = points[num]
        tr, tc, tmax = -1, -1, 0
        for d in range(8):
            ar, ac = r + dr[d], c + dc[d]
            if ar < 0 or ar >= n or ac < 0 or ac >= n:
                continue
            if grid[ar][ac] > tmax:
                tr, tc, tmax = ar, ac, grid[ar][ac]
        points[tmax-1] = (r, c)
        points[num] = (tr, tc)
        grid[tr][tc] = num + 1
        grid[r][c] = tmax
for row in grid:
    for num in row:
        print(num, end=' ')
    print()