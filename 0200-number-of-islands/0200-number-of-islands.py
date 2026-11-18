class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        def dfs(r: int, c: int):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1" or visited[r][c]: return
            visited[r][c] = True
            for d in directions:
                dfs(r+d[0],c+d[1])
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    res += 1
        return res