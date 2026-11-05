class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = max([max(e) for e in edges])
        print(n)

        parent = list(range(n))
        size = [1] * n

        def find(x):
            nonlocal parent
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            nonlocal parent, size
            ra, rb = find(a), find(b)
            if ra == rb: return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return True

        res = None
        for e in edges:
            if not union(e[0]-1, e[1]-1):
                res = e
        return res