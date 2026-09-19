n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 현재 칸 기준으로
# 우하단 직사각형의 칸들 중
# 더 큰 값만 밟을 수 있다.

# i, j 위치의 dp는
# 그 위치에 가기까지의 최대 점프 횟수

# 각 위치별로
# 직전 위치 값을 갖는 메모를 따로 둬야 할까?

dp = [[-1 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1
for i in range(n-1):
    for j in range(m-1):
        if dp[i][j] == 0:
            continue
        for k in range(i+1, n):
            for l in range(j+1, m):
                if grid[k][l] > grid[i][j] and (dp[i][j]+1) > dp[k][l]:
                    dp[k][l] = (dp[i][j]+1)
print(max(max(d) for d in dp))