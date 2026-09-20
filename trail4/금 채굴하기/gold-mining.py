n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# K가 0일 경우, 그 크기는 자기 자신만
# 1이면 자신과 상하좌우
# 2이면 '상하좌우 합쳐서 2까지'
# M이 최대 10이므로 K는 최대 5이다.
# 채굴 비용은 격자 수만큼

# grid 크기에 따라서
# 최대 K는 grid의 높이 // 2 및 grid의 너비 // 2 중 더 큰 쪽

dia = dict()

for k in range(21):
    t = set([(0, 0)])
    for i in range(k+1):
        for j in range(k-i+1):
            t.add((i, j))
            t.add((i, -j))
            t.add((-i, j))
            t.add((-i, -j))
    dia[k] = t

maxK = n

maxi = 0

for k in range(maxK+1):
    price = len(dia[k])
    for i in range(n):
        for j in range(n):
            a = 0
            for x, y in dia[k]:
                ax, ay = x+i, y+j
                if ax >= 0 and ay >= 0 and ax < n and ay < n:
                    a += grid[ax][ay]
            if price <= (a * m):
                maxi = max(maxi, a)
print(maxi)  