n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.
# dp는 n개 두고
# 종료 시점 기준으로 정렬된 dp를 활용한다.
e = sorted(list(enumerate(e)), key = lambda x: x[1])
dp = [0 for _ in range(n+1)]
# dp[i]는 i번째 알바를 할 때 얻을 수 있는 최댓값이다.
ends = -1
ptr = 0
for i in range(n):
    while e[ptr][1] < s[i]:
        j = e[ptr][0]
        if ends == -1 or dp[j] > dp[ends]:
            ends = j
        ptr += 1
    if ends == -1:
        dp[i] = p[i]
    else:
        dp[i] = max(dp[i], dp[ends]+p[i])
print(max(dp))