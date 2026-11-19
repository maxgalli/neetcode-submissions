class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def visit(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            for x, y in directions:
                visit(r + x, c + y)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    visit(i, j)
                    islands += 1
        
        return islands