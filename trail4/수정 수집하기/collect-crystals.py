n, k = map(int, input().split())
str = input()

# Please write your code here.
# i번째 수정이 떨어질 때
# j번 이동해왔다면
# dp[i][j]에 넣는다.
# 1번 수정은 이동 없이 도착할 수 있다.
# 2번 수정부터
# 이동 횟수를 세어준다.
# 홀수 번 움직이면 'R', 짝수 번 움직이면 'L'만 추가 가능하다.
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
if str[0] == 'L':
    dp[1][0] = 1
if str[0] == 'R':
    dp[1][1] = 1
for i in range(2, n+1):
    t = 0 if str[i-1] == 'L' else 1
    for j in range(k+1):
        if j == 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])
        if (j%2)==t:
            dp[i][j]+=1
print(max(dp[-1]))