n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
# cur: 시작 위치
# s: 합
# r: 현재까지의 배열
A=[num for num in A if num <= m]
n = len(A)
A = sorted(A, reverse = True)
dp = [101] * 10001
for num in A:
    for j in range(m,num,-1):
        dp[j] = min(dp[j], dp[j-num]+1)
    dp[num]=1

if dp[m] == 101:
    print(-1)
else:
    print(dp[m])