class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        neighbors = defaultdict(list)
        for u, v, length in edges:
            neighbors[u].append((v, length))
            neighbors[v].append((u, length))

        dist = [inf] * n
        dist[0] = 0
        queue = [(0, 0)]
        while queue:
            curr_dist, curr = heappop(queue)
            if curr_dist > dist[curr]:
                continue
                
            for nxt, length in neighbors[curr]:
                nxt_dist = curr_dist + length
                if nxt_dist < dist[nxt] and nxt_dist < disappear[nxt]:
                    dist[nxt] = nxt_dist
                    heappush(queue, (nxt_dist, nxt))

        return [d if d < inf else -1 for d in dist]
