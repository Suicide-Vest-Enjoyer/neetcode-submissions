class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            req[course].append(pre)

        visiting = set()
        visited = set()

        def dfs(cur):
            if cur in visiting:
                return False

            if cur in visited:
                return True

            visiting.add(cur)

            for pre in req[cur]:
                if not dfs(pre):
                    return False

            visiting.remove(cur)
            visited.add(cur)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True