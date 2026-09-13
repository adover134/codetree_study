n = int(input())
first_cards = list(map(int, input().split()))
second_cards = list(map(int, input().split()))

# Please write your code here.

# i, j, score
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
# dp[i][j]는 first가 i번 카드, second가 j번 카드가 맨 위인 경우이다.
i, j = 0, 0
# dp[i][j]가 값이 있으려면
# 직전에서 i 위치가 j-1 위치보다 컸거나
# i-1, j-1에서 그대로 유지하거나
# i-1 위치가 j 위치보다 작았거나.
for j in range(1, n+1):
    if second_cards[j-1] < first_cards[0]:
        dp[0][j]=second_cards[j-1]+dp[0][j-1]
    else:
        break
for i in range(1, n):
    for j in range(1, n+1):
        a,b,c=0,0,0
        if first_cards[i]>second_cards[j-1]:
            a=dp[i][j-1]+second_cards[j-1]
        b=dp[i-1][j-1]
        if j<n and first_cards[i-1]<second_cards[j]:
            c=dp[i-1][j]
        dp[i][j]=max([a,b,c])
print(max(d[-1] for d in dp))