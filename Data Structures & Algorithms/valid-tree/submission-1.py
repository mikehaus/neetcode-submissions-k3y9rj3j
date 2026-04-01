class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Its a valid tree if all of the edges connect to each other in some way
        if len(edges) > (n - 1):
            return False

        adjGraph = {i: [] for i in range(n)}
        for a, b in edges:
            adjGraph[b].append(a)
            adjGraph[a].append(b)

        visited = set()

        def dfs(cur, prev):
            if cur in visited:
                return False

            visited.add(cur)

            neighbors = adjGraph[cur]
            for n in neighbors:
                if n == prev:
                    continue
                if not dfs(n, cur):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n