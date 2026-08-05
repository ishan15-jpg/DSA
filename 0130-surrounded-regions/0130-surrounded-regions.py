class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited, directions = set(), ((1,0),(0,1),(-1,0),(0,-1))
        def dfs(row: int, col: int) -> None:
            if row < 0 or col < 0 or row == rows or col == cols or (row,col) in visited or board[row][col] != 'O' : return
            visited.add((row,col))
            board[row][col] = 'T'
            for d in directions:
                n_row, n_col = row + d[0], col + d[1]
                dfs(n_row, n_col)
        for c in range(cols):
            if (0,c) not in visited: dfs(0,c)
            if (rows-1,c) not in visited: dfs(rows-1,c)
        for r in range(rows):
            if (r, 0) not in visited: dfs(r,0)
            if (r, cols-1) not in visited: dfs(r, cols-1)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' : board[r][c] = 'X'
                elif board[r][c] == 'T' : board[r][c] = 'O'