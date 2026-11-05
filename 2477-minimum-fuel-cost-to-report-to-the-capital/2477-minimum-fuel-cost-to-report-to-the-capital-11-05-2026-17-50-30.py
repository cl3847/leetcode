class Solution:
    
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        adj_list = defaultdict(list)
        for c1, c2 in roads:
            adj_list[c1].append(c2)
            adj_list[c2].append(c1)

        visited = set([0])
        def helper(node): 
            reps = gas = 0
            for neighbor in adj_list[node]:
                if not neighbor in visited:
                    visited.add(neighbor)
                    dr, dg = helper(neighbor)
                    reps += dr
                    gas += dg + ceil(dr/seats)
            
            reps += 1
            return reps, gas
        
        return helper(0)[1]