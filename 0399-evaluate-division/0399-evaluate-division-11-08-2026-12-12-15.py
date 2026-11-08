class Solution:
    def traverse(self, adj_list, query):
        start, end = query
        if not start in adj_list or not end in adj_list:
            return -1

        dist = defaultdict(lambda: inf)
        dist[start] = 1

        queue = [(1, start)]
        while queue:
            p, curr = heappop(queue)
            for nxt, nxt_cost in adj_list[curr].items():
                prod = p * nxt_cost
                if prod < dist[nxt]:
                    dist[nxt] = prod
                    heappush(queue, (prod, nxt))
        return dist[end]

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(dict)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]

            adj_list[a][b] = val
            adj_list[b][a] = 1/val
        
        res = []
        for query in queries:
            prod = self.traverse(adj_list, query)
            res.append(prod if prod < inf else -1)
        return res


