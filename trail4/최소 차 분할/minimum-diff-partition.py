n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 각 수를 더해 가면서
# 합이 절반을 넘지 않는 최댓값을 구한다.
S = sum(arr)
M = int(S / 2)
arr=sorted(arr, reverse=True)
# 발견한 합 배열을 구한다.
# 합이 절반 이하인 경우들을 구한다.

sums = [False]*(M+1)
for num in arr:
    for m in range(M, num, -1):
        if sums[m-num]:
            sums[m]=True
    sums[num] = True
for m in range(M,0,-1):
    if sums[m]:
        print(S-(m*2))
        break