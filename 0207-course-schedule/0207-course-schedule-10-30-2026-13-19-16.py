class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        nodes = set(range(numCourses))
        while nodes:
            keep = {b for a, b in prerequisites if a in nodes and b in nodes}
            if nodes == keep: return False
            nodes = keep
        return True

