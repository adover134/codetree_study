n = int(input())
coin = [0] + list(map(int, input().split()))

# Please write your code here.
import sys
INT_MIN = -sys.maxsize
dp=[[INT_MIN for _ in range(4)] for _ in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    for j in range(4):
        if j>0:
            dp[i][j]=max(dp[i-2][j], dp[i-1][j-1])+coin[i]
        elif i>1:
            dp[i][j] = dp[i-2][j]+coin[i]
print(max(dp[-1]))