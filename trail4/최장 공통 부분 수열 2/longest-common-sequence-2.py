A = input()
B = input()

# Please write your code here.
la, lb = len(A), len(B)
A, B = [0]+list(A)[::-1], [0]+list(B)[::-1]
from collections import deque
dp = [[0 for j in range(lb+1)] for i in range(la+1)]
path = [[(0, 0) for j in range(lb+1)] for i in range(la+1)]
for i in range(1, la+1):
    for j in range(1, lb+1):
        if dp[i-1][j] > dp[i][j]:
            dp[i][j] = dp[i-1][j]
            path[i][j] = (i-1, j)
        if dp[i][j-1] > dp[i][j]:
            dp[i][j] = dp[i][j-1]
            path[i][j] = (i, j-1)
        if dp[i-1][j-1] >= dp[i][j]:
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            path[i][j] = (i-1, j-1)

i, j = la, lb
while i > 0 and j > 0:
    if path[i][j] == (i-1, j-1) and A[i] == B[j]:
        print(A[i], end='')
    i, j = path[i][j]