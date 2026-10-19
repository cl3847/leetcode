class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lo = 0
        hi = len(self.m[key])
        while lo < hi:
            mid = (lo + hi) // 2
            if self.m[key][mid][1] <= timestamp:
                lo = mid + 1
            else:
                hi = mid
        return self.m[key][lo - 1][0] if lo > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)