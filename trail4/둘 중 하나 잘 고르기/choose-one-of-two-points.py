n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.
# dp[i][j]는 i 장의 카드 중 red를 j 장 고른 경우이다.
dp = [[0 for _ in range(n+1)] for _ in range(n*2)]
dp[0][0] = blue[0]
dp[0][1] = red[0]
for i in range(1, 2*n):
    dp[i][0]=dp[i-1][0]+blue[i]
    for j in range(1,n+1):
        dp[i][j]=max((dp[i-1][j-1]+red[i]), dp[i-1][j]+blue[i])
print(max(d[n] for d in dp))