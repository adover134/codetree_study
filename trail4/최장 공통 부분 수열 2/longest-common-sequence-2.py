A = input()
B = input()

# Please write your code here.
la, lb = len(A), len(B)
from collections import deque
dp = [[0 for i in range(lb+1)] for j in range(la+1)]
visited = [[False for i in range(lb+1)] for j in range(la+1)]
cnt = 0
dq = deque([(0, 0)])
f = False
while dq and f == False:
    for i in range(len(dq)):
        a, b = dq.popleft()
        if visited[a][b]:
            continue
        visited[a][b] = True
        if a == la and b == lb:
            f = True
            break

        aa, bb = a < la, b < lb
        cur = dp[a][b]

        if aa and (dp[a+1][b] <= cur):
            dp[a+1][b] = dp[a][b]
            dq.append((a+1, b))
        if bb and (dp[a][b+1] <= cur):
            dp[a][b+1] = dp[a][b]
            dq.append((a, b+1))
        if aa and bb and (dp[a+1][b+1] <= cur):
            if A[a] == B[b]:
                dp[a+1][b+1] = max(dp[a][b], dp[a+1][b+1])+1
            else:
                dp[a+1][b+1] = max(dp[a][b], dp[a+1][b+1])
            dq.append((a+1, b+1))

i, j = la, lb
ans = ''
while dp[i][j] > 0:
    if dp[i-1][j-1] == (dp[i][j] - 1) and A[i-1]==B[j-1]:
        ans = A[i-1]+ans
        i -= 1
        j -= 1
    elif dp[i-1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1
print(ans)