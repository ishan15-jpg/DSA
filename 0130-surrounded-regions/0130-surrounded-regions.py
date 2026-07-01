class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])

        q = deque([])

        for i in range(n) : 
            if board[0][i] == 'O' : 
                board[0][i] = 'Y'
                q.appendleft((0,i))
            if board[m-1][i] == 'O' : 
                board[m-1][i] = 'Y'
                q.appendleft((m-1,i))
        
        for i in range(m) : 
            if board[i][0] == 'O' : 
                board[i][0] = 'Y'
                q.appendleft((i,0))
            if board[i][n-1] == 'O' : 
                board[i][n-1] = 'Y'
                q.appendleft((i,n-1))


        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while q :
            row,col = q.pop()

            for d in directions:
                nrow, ncol = row + d[0], col + d[1]
                
                if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n and board[nrow][ncol] == 'O' :
                    board[nrow][ncol] = 'Y'
                    q.appendleft((nrow,ncol))

        for r in range(m) :
            for c in range(n) :
                if board[r][c] == 'O' : board[r][c] = 'X'
                elif board[r][c] == 'Y' : board[r][c] = 'O'
