n = int(input())
profit = list(map(int, input().split()))

# Please write your code here.
# 각 길이의 합을 통해
# 최대 값을 얻는 것이 목표
values = [0]
values.extend([p for p in profit])
for i in range(1, n+1):
    for j in range(1, i+1):
        values[i] = max((profit[j-1]+values[i-j]), values[i])
print(values[-1])