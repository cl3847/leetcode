class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        original = transactions
        transactions = [tuple(t.split(",")) + (i,) for i, t in enumerate(transactions)]
        transactions.sort(key=lambda t: int(t[1]))

        res = set()
        window = defaultdict(lambda: defaultdict(set))
        l = 0
        for r in range(len(transactions)):
            name, time, amount, city, _ = transactions[r]
            time, amount = int(time), int(amount)
            while time - int(transactions[l][1]) > 60:
                old_name, old_city = transactions[l][0], transactions[l][3]
                window[old_name][old_city].remove(transactions[l])
                if not window[old_name][old_city]:
                    del window[old_name][old_city]   # fix 4: empty cities stop counting
                l += 1

            window[name][city].add(transactions[r])
            if len(window[name]) > 1:
                for s in window[name].values():
                    res |= s

            if amount > 1000:
                res.add(transactions[r])
        return [original[t[4]] for t in res]