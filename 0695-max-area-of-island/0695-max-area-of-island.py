class Solution:
    def __init__(self):
        self.directions: tuple(tuple(int)) = ((1,0),(0,1),(-1,0),(0,-1))

    def dfs(self, r: int, c: int, visited: list[list[int]], grid: list[list[int]]) -> int:
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1 or visited[r][c]: return 0
        visited[r][c] = True
        res = 1
        for d in self.directions:
            res += self.dfs(r+d[0],c+d[1],visited,grid)
        return res

    def bfs(self, r: int, c: int, visited: list[list[int]], grid: list[list[int]]) -> int:
        visited[r][c] = True
        queue = [(r,c)]
        res = 1
        while queue:
            r,c = queue.pop(0)
            for d in self.directions:
                nr,nc = r+d[0],c+d[1]
                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    res += 1
                    queue.append((nr,nc))
        return res
    
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and not visited[r][c]:
                    res = max(res,self.bfs(r,c,visited,grid))
        return res