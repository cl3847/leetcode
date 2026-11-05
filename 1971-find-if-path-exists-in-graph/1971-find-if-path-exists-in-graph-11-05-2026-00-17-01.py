class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
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

        for e in edges:
            union(e[0], e[1])
        
        return find(source) == find(destination)
