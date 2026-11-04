class NumberContainers:

    def __init__(self):
        self.indices = {}
        self.nums = defaultdict(list)    

    def change(self, index: int, number: int) -> None:
        self.indices[index] = number
        heappush(self.nums[number], index)

    def find(self, number: int) -> int:
        while self.nums[number]:
            lowest = self.nums[number][0]
            if not self.indices[lowest] == number:
                heappop(self.nums[number])
                continue
            return lowest   
        return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)