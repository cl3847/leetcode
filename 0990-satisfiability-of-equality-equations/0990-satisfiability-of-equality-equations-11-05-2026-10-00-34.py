class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        parent = {}
        size = defaultdict(lambda: 1)
        equalities, inequalities = [], []
        for e in equations:
            x, op, y = e[0], e[1:3], e[3]
            parent[x] = x
            parent[y] = y
            if op == "==": 
                equalities.append((x, y))
            else:
                inequalities.append((x, y))

        def find(x):
            nonlocal parent
            while x != parent[x]:
                parent[x] == parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            nonlocal parent, size
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[ra] = rb
            size[rb] += 1
            return True

        for eq in equalities:
            union(eq[0], eq[1])
        
        for ineq in inequalities:
            if find(ineq[0]) == find(ineq[1]):
                return False
        return True