n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.
# dp는 k 값에 따라 층 수를 바꿔주자.
import sys
INT_MIN=-sys.maxsize
dp=[[INT_MIN for _ in range(k+1)] for _ in range(n)]
if numbers[0]<0:
    dp[0][1]=numbers[0]
else:
    dp[0][0] = numbers[0]
for i in range(1,n):
    if numbers[i]<0:
        dp[i][1]=max((dp[i-1][0]+numbers[i]), numbers[i])
        for j in range(2,k+1):
            dp[i][j] = dp[i-1][j-1]+numbers[i]
    else:
        dp[i][0]=max((dp[i-1][0]+numbers[i]), numbers[i])
        for j in range(1,k+1):
            dp[i][j]=dp[i-1][j]+numbers[i]
print(max(max(d) for d in dp))