A = input()
B = input()

# Please write your code here.
# i까지 봤을 때
# j까지 일치하게 하려면
# i번째와 j번째가 같을 경우 [i-1][j-1]에서의 dp 값과 같을 수 있다. (추가 조작 불필요)
    # 이외에는 공통적으로
    # dp[i-1][j]+1 (이미 i-1에서 j까지 만들었으니 하나 지운다.)
    # dp[i][j-1]+1 (j-1까지 만든 상태에서 하나 더해서 j까지 만든다.)
    # dp[i-1][j-1]+1 (A의 i번째와 B의 j번째가 서로 다르므로 바꾼다.)
la, lb = len(A), len(B)
dp = [[0 for _ in range(lb+1)] for _ in range(la+1)]
for i in range(1, la+1):
    dp[i][0] = i
for j in range(1, lb+1):
    dp[0][j] = j
for i in range(1, la+1):
    for j in range(1, lb+1):
        ne = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1
        if A[i-1] == B[j-1]:
            ne = min(dp[i-1][j-1], ne)
        dp[i][j] = ne
print(dp[la][lb])