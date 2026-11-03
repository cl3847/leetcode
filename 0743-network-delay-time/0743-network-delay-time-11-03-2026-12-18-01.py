class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        neighbors = defaultdict(list)
        for u, v, w in times:
            neighbors[u].append((w, v))

        dist = [math.inf] * (n+1)
        dist[k] = 0
        queue = []
        heappush(queue, (0, k))
        visited = set()
        while queue:
            t, curr = heappop(queue)
            if curr in visited: continue
            visited.add(curr)
            for dt, n in neighbors[curr]:
                if t+dt < dist[n]:
                    dist[n] = t+dt
                    heappush(queue, (t+dt, n))
        dist[0] = -math.inf
        res = max(dist)
        return res if res < math.inf else -1


            
