A = input()
B = input()

# Please write your code here.
la, lb = len(A), len(B)
from collections import deque
from copy import deepcopy
dq = deque([(0, 0)])
dp = [[-1 for _ in range(lb+1)] for _ in range(la+1)]
dp[0][0] = 0
cnt = 1
f = False
# dp[i][j]는
# dp[i+1][j]보다 1 작거나
# dp[i][j+1]보다 1 작거나
# dp[i+1][j+1]보다 1 작음
# 하지만 A[i]와 B[j]가 같으면
# dp[i+1][j+1]과 같음
while dq and not f:
    for _ in range(len(dq)):
        i, j = dq.popleft()
        t = deque([(i, j)])
        while i < la and j < lb and A[i] == B[j]:
            i += 1
            j += 1
            t.append((i, j))
            if dp[i][j] == -1:
                dp[i][j] = cnt - 1
            else:
                break
        while t:
            i, j = t.popleft()
            if i < la and dp[i+1][j] == -1:
                    dp[i+1][j] = cnt
                    dq.append((i+1, j))
            if j < lb and dp[i][j+1] == -1:
                    dp[i][j+1] = cnt
                    dq.append((i, j+1))
    if dp[la][lb] >= 0:
        break
    cnt += 1
print(dp[-1][-1])