class StockSpanner:

    def __init__(self):
        self.stack = [(math.inf, -1)] # (price, day)
        self.day = 0

    def next(self, price: int) -> int:
        while self.stack[-1][0] <= price:
            self.stack.pop()

        res = self.day - self.stack[-1][1]
        self.stack.append((price, self.day))
        self.day += 1
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)