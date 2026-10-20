class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        counts = defaultdict(lambda: defaultdict(int))
        food_types = set()
        for customer, table, item in orders:
            counts[table][item] += 1
            food_types.add(item)

        food_index = {item: i for i, item in enumerate(sorted(food_types))}
        res = [["Table"] + [item for item in food_index]]
        for table in sorted(counts, key=int):
            row = ["0"] * (len(food_index) + 1)
            row[0] = table
            for order in counts[table].items():
                row[food_index[order[0]] + 1] = str(order[1])
            res.append(row)
        return res  
