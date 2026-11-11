class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)
        for i, edge in enumerate(edges):
            a, b = edge
            adj_list[a].append((b, succProb[i]))
            adj_list[b].append((a, succProb[i]))

        probs = [0] * n
        queue = [(1, start_node)]

        while queue:
            prob, curr = heappop_max(queue)
            if curr == end_node:
                return prob

            for nxt, dp in adj_list[curr]:
                nxt_prob = prob * dp
                if probs[nxt] == 0 or nxt_prob > probs[nxt]:
                    probs[nxt] = nxt_prob
                    heappush_max(queue, (nxt_prob, nxt))

        return 0
