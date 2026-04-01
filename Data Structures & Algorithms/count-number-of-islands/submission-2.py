class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited: Set[Tuple[int, int]] = set()
        x, y, max_x, max_y = 0, 0, len(grid[0]), len(grid)
        for x in range(max_x):
            for y in range(max_y):
                if not (x, y) in visited and grid[y][x] == "1":
                    self.dfs(x, y, grid, visited)
                    res += 1
        return res

    def dfs(self, x: int, y: int, grid: List[List[str]], visited: Set[Tuple[int, int]]) -> None:
        max_x, max_y = len(grid[0]), len(grid)
        if x == max_x or y == max_y or x < 0 or y < 0:
            return
        if grid[y][x] == "0":
            return
        if (x, y) in visited:
            return
        visited.add((x, y))
        self.dfs(x - 1, y, grid, visited)
        self.dfs(x, y - 1, grid, visited)
        self.dfs(x + 1, y, grid, visited)
        self.dfs(x, y + 1, grid, visited)