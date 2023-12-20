#dp knight problem
board = [[None] * 8 for i in range(8)]
stack = [[1,6]]
board[1][6] = 0
moves = [[1,2], [1,-2], [-2,1], [-2,-1], [2,1], [2,-1], [-1,2], [-1,-2]]
while stack:
    i, j = stack.pop()
    for k in moves:
        if i+k[0] >= 0 and i+k[0] < 8 and j+k[1] >=0 and j+k[1] < 8:
            if board[i+k[0]][j+k[1]] == None or (board[i][j] + 1) < board[i+k[0]][j+k[1]]:
                board[i+k[0]][j+k[1]] = board[i][j] + 1
                stack.append([i+k[0], j+k[1]])
for i in board:
    print(*i)




a = "abaaba"
b = "babbab"
dp = [[0]*(len(b)+1) for i in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(*dp,sep='\n')

