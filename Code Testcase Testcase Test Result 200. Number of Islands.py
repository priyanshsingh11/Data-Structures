class Solution(object):

    def dfs(self, r, c, grid, visited, rows, cols):
        if (
            r < 0 or r >= rows or
            c < 0 or c >= cols or
            grid[r][c] != '1' or
            visited[r][c]
        ):
            return

        visited[r][c] = True

        self.dfs(r + 1, c, grid, visited, rows, cols)
        self.dfs(r - 1, c, grid, visited, rows, cols)
        self.dfs(r, c + 1, grid, visited, rows, cols)
        self.dfs(r, c - 1, grid, visited, rows, cols)

    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        ans = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    ans += 1
                    self.dfs(r, c, grid, visited, rows, cols)

        return ans
