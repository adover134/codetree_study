n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# Please write your code here.
# r, c 위치에서 시작
# m1, m2, m3, m4, dir이고
# m1과 m3, m2와 m4는 같을 것이고
# dir는 0이면 반시계, 1이면 시계
r, c = r-1, c-1
t = grid[r][c]
if dir == 0:
    for i in range(m2):
        grid[r][c] = grid[r-1][c-1]
        r, c= r-1, c-1
    for i in range(m1):
        grid[r][c] = grid[r-1][c+1]
        r, c = r-1, c+1
    for i in range(m2):
        grid[r][c] = grid[r+1][c+1]
        r, c = r+1, c+1
    for i in range(m1):
        grid[r][c] = grid[r+1][c-1]
        r, c = r+1, c-1
    grid[r-1][c+1] = t
else:
    for i in range(m1):
        grid[r][c] = grid[r-1][c+1]
        r, c= r-1, c+1
    for i in range(m2):
        grid[r][c] = grid[r-1][c-1]
        r, c = r-1, c-1
    for i in range(m1):
        grid[r][c] = grid[r+1][c-1]
        r, c = r+1, c-1
    for i in range(m2):
        grid[r][c] = grid[r+1][c+1]
        r, c = r+1, c+1
    grid[r-1][c-1] = t
for g in grid:
    for num in g:
        print(num, end=' ')
    print()