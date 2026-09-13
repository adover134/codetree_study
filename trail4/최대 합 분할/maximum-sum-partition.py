n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
m = sum(arr)
# 만들 수 있는 모든 subset을 구한 뒤
# 나머지에서 동일한 합이 가능한지 보기?

# i번째 수까지 봤을 때
# 두 그룹 사이의 차이가 0인 경우 구하기?

# 전체 최대 합은 100000
# i번째 행에서의 값은
# A/B 차이가 j일 때 A의 합?
offset = m+1
import sys
INT_MIN = -sys.maxsize
dp=[
    [0] * (m+offset+1) for _ in range(n+1)
]
for i in range(n+1):
    for j in range(-m+offset, m+offset+1):
        dp[i][j] = INT_MIN
dp[0][offset] = 0
for i in range(n):
    for j in range(-m+offset, m+offset):
        if dp[i][j] != INT_MIN:
            if (j+arr[i])<=(m+offset):
                if dp[i+1][j+arr[i]] < (dp[i][j]+arr[i]):
                    dp[i+1][j+arr[i]]=dp[i][j]+arr[i]
            if (j-arr[i]) >= 0:
                if dp[i+1][j-arr[i]] < dp[i][j]:
                    dp[i+1][j-arr[i]]=dp[i][j]
            if dp[i+1][j] < dp[i][j]:
                dp[i+1][j]=dp[i][j]
print(dp[-1][offset])