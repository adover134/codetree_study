n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
print(a[r][c], end = ' ')
while True:
    tr, tc = r, c
    f = False
    for d in range(4):
        ar, ac = r + dr[d], c + dc[d]
        if ar < 0 or ar > n or ac < 0 or ac > n:
            continue
        if a[ar][ac] > a[r][c]:
            r, c = ar, ac
            f = True
            break
    if f:
        print(a[r][c], end = ' ')
    else:
        break
