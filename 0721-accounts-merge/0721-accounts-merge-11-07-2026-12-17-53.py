class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        parent = {}
        size = defaultdict(lambda: 1)
        def find(x):
            nonlocal parent
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            nonlocal parent, size
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
            return True
                
        names = {}
        for acc in accounts:
            name, emails = acc[0], acc[1:]
            rep = emails[0]
            for e in emails:
                parent[e] = parent.get(e, e)
                names[e] = name
                union(rep, e)

        groups = defaultdict(list)
        for p in parent:
            groups[find(p)].append(p)
        
        return [[names[p]] + sorted(groups[p]) for p in groups]




        
        
