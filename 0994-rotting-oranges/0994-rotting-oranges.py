class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque([])
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0: return 0
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        res = 0
        while queue and fresh:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for d in directions:
                    nr,nc = r+d[0],c+d[1]
                    if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))
            res += 1
        return res if fresh == 0 else -1