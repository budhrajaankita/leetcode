# Last updated: 6/11/2025, 10:34:43 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        g = defaultdict(list)

        for a, b in prerequisites:
            g[a].append(b)

        visited = [0] * numCourses

        # unvisited: 0; visited=2; visiting=1
        def hasCycle(course):
            if visited[course] == 2:
                return False
            if visited[course] == 1:
                return True

            visited[course] = 1

            for courses in g[course]:
                if hasCycle(courses):
                    return True

            visited[course] = 2

            # return False

        
        for course in range(numCourses):
            if hasCycle(course): return False

        return True

        