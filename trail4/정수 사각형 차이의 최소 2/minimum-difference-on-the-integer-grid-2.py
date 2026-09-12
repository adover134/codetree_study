n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
mini =set(g for c in grid for g in c)
res = [[{k: [0,-1] for k in mini} for _ in range(n)] for _ in range(n)]
# 각 키마다 [max, diff]
res[0][0][grid[0][0]] = [grid[0][0], 0]
for i in range(1, n):
    for k in mini:
        if res[i-1][0][k][1] > -1:
            # 만약 현재 값이 더 작다면
            # 갱신하거나
            # 그대로 넣는다.
            if grid[i][0] < k:
                if (res[i][0][grid[i][0]][1]) == -1 or (res[i][0][grid[i][0]][1] > res[i-1][0][k][0]-grid[i][0]):
                    res[i][0][grid[i][0]] = [res[i-1][0][k][0], res[i-1][0][k][0]-grid[i][0]]
            elif grid[i][0] > res[i-1][0][k][0]:
                res[i][0][k] = [grid[i][0], grid[i][0]-k]
            # 만약 현재 값이
            # 기존의 k에 대해
            # 그 사이의 값이라면
            # 기존의 갭과
            # 현재 갭을 비교해야 된다.
            else:
                res[i][0][k] = res[i-1][0][k]
        if res[0][i-1][k][1] > -1:
            if grid[0][i] < k:
                if (res[0][i][grid[0][i]][1]) == -1 or (res[0][i][grid[0][i]][1] > res[0][i-1][k][0]-grid[0][i]):
                    res[0][i][grid[0][i]] = [res[0][i-1][k][0], res[0][i-1][k][0]-grid[0][i]]
            elif grid[0][i] > res[0][i-1][k][0]:
                res[0][i][k] = [grid[0][i], grid[0][i]-k]
            else:
                res[0][i][k] = res[0][i-1][k]

for i in range(1, n):
    for j in range(1, n):
        for k in mini:
            # 만약 이전 위치에서, 최솟값이 k인 경우가 있다면
            if res[i-1][j][k][1] > -1:
                # 만약 현재 값이 k보다 작다면
                if grid[i][j] < k:
                    # 만약 현재 값이 최소인 경우가 아직 안 찾아졌거나
                    # 현재 값이 최소인 경우에 대해 기존 차가 더 크다면
                    if (res[i][j][grid[i][j]][1] == -1) or (res[i][j][grid[i][j]][1] > res[i-1][j][k][0]-grid[i][j]):
                        res[i][j][grid[i][j]] = [res[i-1][j][k][0], res[i-1][j][k][0]-grid[i][j]]
                elif grid[i][j] > res[i-1][j][k][0]:
                    res[i][j][k] = [grid[i][j], grid[i][j]-k]
                elif res[i][j][k][1] == -1 or res[i][j][k][1] > res[i-1][j][k][1]:
                    res[i][j][k] = res[i-1][j][k]
            if res[i][j-1][k][1] > -1:
                if grid[i][j] < k:
                    if (res[i][j][grid[i][j]][1] == -1) or (res[i][j][grid[i][j]][1] > res[i][j-1][k][0]-grid[i][j]):
                        res[i][j][grid[i][j]] = [res[i][j-1][k][0], res[i][j-1][k][0]-grid[i][j]]
                elif grid[i][j] > res[i][j-1][k][0]:
                    res[i][j][k] = [grid[i][j], grid[i][j]-k]
                elif res[i][j][k][1] == -1 or res[i][j][k][1] > res[i][j-1][k][1]:
                    res[i][j][k] = res[i][j-1][k]
print(min(res[n-1][n-1][k][1] if res[n-1][n-1][k][1] > -1 else float('inf') for k in mini))