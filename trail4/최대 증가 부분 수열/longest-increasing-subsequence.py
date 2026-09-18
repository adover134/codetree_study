n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
# 각 숫자는
# 그 위치에서의 숫자이다.
# 숫자들 중 임의로 뽑아서
# i번 숫자 기준으로
# 이전 숫자가 j일 때
# 최대 개수를 구한다.
dp = [-1 for _ in range(max(m)+1)]
dp[0] = 0
for i in range(n):
    a = m[i]
    for j in range(a):
        if (dp[j]+1) > dp[a]:
            dp[a] = dp[j] + 1
print(max(dp))