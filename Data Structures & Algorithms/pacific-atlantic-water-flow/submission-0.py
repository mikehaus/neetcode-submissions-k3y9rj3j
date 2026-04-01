class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        # Don't add any duplicates
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            # Check in visited or OOB or if cur is less than prev, return
            if ((r, c) in visited or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return
            # Add current to visited
            visited.add((r, c))
            # Recurse all directions
            cur_h = heights[r][c]
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # for every column, dfs for pacific from start of pacific (0, max_x)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # for every row, dfs for atlantic from start of atlantic (max_y, 0)
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        # search for every where values in sets and append to result
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        # return result
        return res


        

       