class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        unlocks = [[] for _ in range(numCourses)]
        needed = [0] * numCourses
        for a, b in prerequisites:
            unlocks[b].append(a)
            needed[a] += 1
        queue = deque([i for i in range(numCourses) if needed[i] == 0])
        
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for nxt in unlocks[course]:
                needed[nxt] -= 1
                if needed[nxt] == 0:
                    queue.append(nxt)
        return res
        
