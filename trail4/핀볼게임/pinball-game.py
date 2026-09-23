n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 맨 위 칸에 대해 위에서 주는 경우
# 맨 왼쪽 칸에 대해 오른쪽으로 미는 경우
# 맨 오른쪽 칸에 대해 왼쪽으로 미는 경우
# 맨 아래 칸에 대해 위로 올리는 경우

# 이 4가지를 각각 테스트해야 된다.
memo = [[{'D': -1, 'U': -1, 'R': -1, 'L': -1} for _ in range(n)] for _ in range(n)]

def move(dir, r, c):
    if r < 0 or c < 0 or r >= n or c >= n:
        return 1
    cnt = 1
    if memo[r][c][dir] > 0:
        return memo[r][c][dir]
    else:
        match dir:
            case 'D':
                match grid[r][c]:
                    case 0:
                        cnt += move('D', r+1, c)
                    case 1:
                        cnt += move('L', r, c-1)
                    case 2:
                        cnt += move('R', r, c+1)
            case 'U':
                match grid[r][c]:
                    case 0:
                        cnt += move('U', r-1, c)
                    case 1:
                        cnt += move('R', r, c+1)
                    case 2:
                        cnt += move('L', r, c-1)
            case 'R':
                match grid[r][c]:
                    case 0:
                        cnt += move('R', r, c+1)
                    case 1:
                        cnt += move('U', r-1, c)
                    case 2:
                        cnt += move('D', r+1, c)
            case 'L':
                match grid[r][c]:
                    case 0:
                        cnt += move('L', r, c-1)
                    case 1:
                        cnt += move('D', r+1, c)
                    case 2:
                        cnt += move('U', r-1, c)
        memo[r][c][dir] = cnt
        return cnt
maxi = 0
for i in range(n):
    maxi = max([move('D', 0, i), move('U', n-1, i), move('R', i, 0), move('L', i, n-1), maxi])
print(maxi)