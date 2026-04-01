class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 2:
            return True

        g = defaultdict(list)
        for post, pre in prerequisites:
            g[post].append(pre)
        
        visited = set()

        def isValid(cur):
            if cur in visited:
                return False
            if g[cur] == []:
                return True
            visited.add(cur)

            for n in g[cur]:
                if not isValid(n):
                    return False

            visited.remove(cur)
            g[cur] = []
            return True

        for course in range(numCourses):
            if not isValid(course):
                return False
        return True