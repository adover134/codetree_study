A = input()
B = input()

# Please write your code here.
# dp[i][j]는
# A의 i번째 문자
# B의 j번째 문자까지 봤을 때
# 그 시점까지의 최장 공통 부분 수열의 길이를 저장한다.

# 만약 A[i]와 B[j]가 같다면
    # dp[i-1][j-1]에서 1 추가할 수 있다.
# 공통적으로는
    # dp[i-1][j] 혹은
    # dp[i][j-1]을 그대로 가져올 수 있다.
    # 이 두 경우는 그냥 한 쪽만 더 가져온 경우이다.

# 여기서 i는 1부터 len(A) 까지로 나타낸다.

la, lb = len(A), len(B)
dp = [[0 for _ in range(lb+1)] for _ in range(la+1)]
for i in range(1, la+1):
    for j in range(1, lb+1):
        ne = max(dp[i-1][j], dp[i][j-1])
        if A[i-1] == B[j-1]:
            ne = max(ne, dp[i-1][j-1]+1)
        dp[i][j] = ne
print(dp[-1][-1])