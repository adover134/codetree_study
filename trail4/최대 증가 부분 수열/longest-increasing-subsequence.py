n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
# 각 숫자는
# 그 위치에서의 숫자이다.
# 숫자들 중 임의로 뽑아서
# i번 숫자 기준으로
# 이전 숫자가 j일 때
# 최대 개수를 구한다.
dp = [1 for _ in range(n+1)]
dp[1] = 1
for i in range(1, n+1):
    maxi = 0
    for j in range(1, i):
        if m[j-1] < m[i-1]:
            maxi = max(maxi, dp[j])
    dp[i] = maxi + 1
print(max(dp))