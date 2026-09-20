n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 현재 점에서 만들 수 있는 직사각형은
# 현재 위치가 [i][j]일 때
# i 칸까지 왼쪽 이동 가능
# n-i-1 칸까지 우측 이동 가능
# 아래로는 둘을 합쳐서 [n-j-1] 칸까지 가능
maxi = 0
for i in range(1, n):
    for j in range(n):
        for a in range(1, i+1):
            for b in range(1, n-i):
                if (a + b + j) >= n:
                    break
                s = 0
                for ii in range(1, a+1):
                    i, j = i - 1, j + 1
                    s += grid[i][j]
                for ii in range(1, b+1):
                    i, j = i + 1, j + 1
                    s += grid[i][j]
                for ii in range(1, a+1):
                    i, j = i + 1, j - 1
                    s += grid[i][j]
                for ii in range(1, b+1):
                    i, j = i - 1, j - 1
                    s += grid[i][j]
                maxi = max(s, maxi)
print(maxi)