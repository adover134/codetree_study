n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
area_set = dict()
for i in range(n):
    for j in range(m):
        for h in range(1, n-i+1):
            g = grid[i:i+h]
            for w in range(1, m-j+1):
                a = 0
                for line in g:
                    a += sum(line[j:j+w])
                area_set[(i, j, h, w)] = a
maxi = -26000
for ax in range(n):
    for ah in range(1, n-ax+1):
        for ay in range(m):
            for aw in range(1, m-ay+1):
                for bx in range(n):
                    for bh in range(1, n-bx+1):
                        for by in range(m):
                            for bw in range(1,m-by+1):
                                if bx >= ax+ah or by >= ay+aw or ax >= bx+bh or ay >= by+bw:
                                    aa = area_set[(ax,ay,ah,aw)]
                                    bb = area_set[(bx,by,bh,bw)]
                                    maxi = max(aa+bb, maxi)
print(maxi)