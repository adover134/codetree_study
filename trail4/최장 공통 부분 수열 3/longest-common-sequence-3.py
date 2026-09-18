n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
# 역순 기준으로
# dp[i][j]는
# a[i] 및 b[j]까지 봤을 때의 LCS의 길이이다.
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
a = [0]+a[::-1]
b = [0]+b[::-1]
from collections import deque
# 현재 이 칸 다음 칸들 중
# LCS의 마지막 숫자가 가장 작은 칸 추적
cur_best = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
path = [[(0, 0) for _ in range(m+1)] for _ in range(n+1)]
f = False
for i in range(1, n+1):
    for j in range(1, m+1):
        # i-1/j-1 위치가 같은 경우
        # cur_best[i][j]는 a[i]가 되며
        # path[i][j]는 (i-1, j-1)이 된다.
        # dp[i][j] 는 1 증가
        if dp[i-1][j] > dp[i][j] or (dp[i-1][j] == dp[i][j] and cur_best[i][j] > cur_best[i-1][j]):
            dp[i][j] = dp[i-1][j]
            path[i][j] = (i-1, j)
            cur_best[i][j] = cur_best[i-1][j]
        if dp[i][j-1] > dp[i][j] or (dp[i][j-1] == dp[i][j] and cur_best[i][j] > cur_best[i][j-1]):
            dp[i][j] = dp[i][j-1]
            path[i][j] = (i, j-1)
            cur_best[i][j] = cur_best[i][j-1]
        if a[i] == b[j] and ((dp[i-1][j-1]+1)>dp[i][j] or ((dp[i-1][j-1]+1)==dp[i][j] and a[i] < cur_best[i][j])):
            dp[i][j] = dp[i-1][j-1]+1
            path[i][j] = (i-1, j-1)
            cur_best[i][j] = a[i]

i, j = n, m
ans = []
while i>0 and j>0:
    if path[i][j] == (i-1, j-1) and a[i] == b[j]:
        print(a[i], end=' ')
    i, j = path[i][j]