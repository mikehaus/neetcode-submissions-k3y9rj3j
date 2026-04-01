class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 2:
            return True

        # first build out our graph
        g = {i: [] for i in range(numCourses)}
        for post, pre in prerequisites:
            g[post].append(pre)

        visited = set()

        # Next do dfs on graph to see if fits constraints
        # Prerequisites are a DAG, where if there is a cycle, it is not valid
        # We need to do a dfs
        def coursesValid(cur):
            if cur in visited:
                return False
            if g[cur] == []:
                return True
            visited.add(cur)
                
            for neighbor in g[cur]:
                if not coursesValid(neighbor):
                    return False
            visited.remove(cur)
            g[cur] = []
            return True

        print(g)

        for course in range(numCourses):
            if not coursesValid(course):
                return False
        return True

        