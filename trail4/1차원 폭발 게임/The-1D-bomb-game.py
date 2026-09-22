n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.
while numbers:
    f = False
    cur = 0
    cnt = 1
    stack = []
    for i in range(1, len(numbers)):
        if numbers[cur] == numbers[i]:
            cnt += 1
        else:
            if cnt >= m:
                stack.append((cur, cnt))
            cur = i
            cnt = 1
    if cnt >= m:
        stack.append((cur, cnt))
    if not stack:
        break
    while stack:
        cur, cnt = stack.pop()
        numbers = numbers[:cur]+numbers[cur+cnt:]

print(len(numbers))
for number in numbers:
    print(number)