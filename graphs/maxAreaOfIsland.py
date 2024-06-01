
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 0  # Mark as visited by setting to 0
            area = 1  # Start with the initial cell

            while stack:
                row, col = stack.pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        stack.append((new_row, new_col))
                        grid[new_row][new_col] = 0  # Mark as visited
                        area += 1  # Increment the area for each new cell added to the island
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        
        return maxArea