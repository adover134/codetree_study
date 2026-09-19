n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
# 2개의 DP가 필요하다.
# 현재 위치까지의 증가하는 부분 수열의 길이
# 역방향으로, 현재 위치까지의 증가하는 부분 수열의 길이

increasing = [1 for _ in range(n)]
decreasing = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if sequence[i] > sequence[j] and increasing[i] < (increasing[j]+1):
            increasing[i] = increasing[j]+1
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if sequence[i] > sequence[j] and decreasing[i] < (decreasing[j]+1):
            decreasing[i] = decreasing[j]+1
print(max(a+b for (a,b) in zip(increasing, decreasing))-1)