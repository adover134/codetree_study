n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
for r1,c1,r2,c2 in winds:
    t = a[r1-1][c2-1]
    for c in range(c2-1, c1-1, -1):
        a[r1-1][c] = a[r1-1][c-1]
    for r in range(r1-1, r2-1):
        a[r][c1-1] = a[r+1][c1-1]
    for c in range(c1-1, c2-1):
        a[r2-1][c] = a[r2-1][c+1]
    for r in range(r2-1, r1, -1):
        a[r][c2-1] = a[r-1][c2-1]
    a[r1][c2-1] = t
    t = []
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    for r in range(r1-1, r2):
        tr = []
        for c in range(c1-1, c2):
            s = a[r][c]
            cnt = 1
            for d in range(4):
                ax, ay = dx[d]+r, dy[d]+c
                if ax < 0 or ax == n or ay < 0 or ay == m:
                    continue
                s += a[ax][ay]
                cnt += 1
            tr.append(s//cnt)
        t.append(tr)
    for r in range(r1-1, r2):
        a[r][c1-1:c2] = t[r-r1+1]
for r in a:
    for num in r:
        print(num, end = ' ')
    print()