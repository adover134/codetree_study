n, t = map(int, input().split())

belt = [list(map(int, input().split())) for _ in range(3)]

# Please write your code here.
# N초마다 다음 줄의 첫 숫자가 이 줄로 들어온다.
t %= 3*n
w, p = t // n, t % n
for i in range(3):
    line_start = (3 - w + i) % 3
    if p > 0:
        for num in belt[(line_start+2)%3][-p:]+belt[line_start][:n-p]:
            print(num, end=' ')
    else:
        for num in belt[line_start]:
            print(num, end=' ')
    print()