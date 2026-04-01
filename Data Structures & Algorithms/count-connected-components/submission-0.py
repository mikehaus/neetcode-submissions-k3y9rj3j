class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 1:
            return 1
        adj = {i: [] for i in range(n)}
        for v, e in edges:
            adj[v].append(e)
            adj[e].append(v)

        visited = [False] * n

        # need to find amount of cycles in a graph
        # if visited we know there is a cycle so we can remove
        def dfs(cur):
            for nei in adj[cur]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1
        return res
                

                

        