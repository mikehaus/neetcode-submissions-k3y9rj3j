class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.find_islands(grid)

    def find_islands(self, grid) -> int:
        island_count = 0
        end_x, end_y = len(grid[0]) - 1, len(grid) - 1
        cur_x, cur_y = 0, 0

        while cur_y <= end_y:
            cur = grid[cur_y][cur_x]
            print(cur)
            if cur == "1":
                self.dfs(grid, cur_x, cur_y, end_x, end_y)
                island_count += 1
            cur_x += 1
            if cur_x > end_x:
                cur_x = 0
                cur_y += 1

        return island_count

    def dfs(self, grid, x, y, max_x, max_y):
        stack = [[x, y]]
        grid[y][x] = "0"

        while stack:
            cur = stack.pop()
            x, y = cur  

            neighbors = [
                self.up(x, y),
                self.down(x, y, max_y),
                self.left(x, y),
                self.right(x, y, max_x)
            ]

            for neighbor in neighbors:
                if neighbor and grid[neighbor[1]][neighbor[0]] == "1":
                    stack.append(neighbor)
                    grid[neighbor[1]][neighbor[0]] = "0"
             
    def up(self, x, y):
        if y - 1 < 0:
            return None
        return [x, y - 1]

    def down(self, x, y, max_y):
        if y + 1 > max_y:
            return None
        return [x, y + 1]
    
    def left(self, x, y):
        if x - 1 < 0:
            return None
        return [x - 1, y]
    
    def right(self, x, y, max_x):
        if x + 1 > max_x:
            return None
        return [x + 1, y]
