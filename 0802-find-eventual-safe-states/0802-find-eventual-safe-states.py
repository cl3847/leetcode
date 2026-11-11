class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        unlocks = [[] for _ in range(n)]
        needed = [0] * n
        for i, neighbors in enumerate(graph):
            for n in neighbors:
                unlocks[n].append(i)
                needed[i] += 1
        
        safe = [i for i, n in enumerate(needed) if n == 0]
        queue = deque(safe)
        while queue:
            curr = queue.popleft()
            for nxt in unlocks[curr]:
                needed[nxt] -= 1
                if needed[nxt] == 0:
                    safe.append(nxt)
                    queue.append(nxt)
                
        return sorted(safe)