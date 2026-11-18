class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        res = 0
        while queue:
            s = len(queue)
            rot = False
            for _ in range(s):
                r,c = queue.popleft()
                for d in directions:
                    nr,nc = r+d[0],c+d[1]
                    if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == 1:
                        rot = True
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
            if rot: res += 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: return -1
        return res