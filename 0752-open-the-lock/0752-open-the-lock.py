class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends = set(deadends)
        queue = deque(['0000'])
        layer = 0
        visited = set()
        while queue:
            for _ in range(len(queue)):
                comb = queue.popleft()
                if comb in deadends:
                    continue
                elif comb == target:
                    return layer
                
                nums = [int(n) for n in comb]
                for i in range(4):
                    for j in [-1, 1]:
                        nums[i] = (nums[i] + j) % 10
                        nxt = ''.join([str(n) for n in nums])
                        if not nxt in visited:
                            visited.add(nxt)
                            queue.append(nxt)
                        nums[i] = (nums[i] - j) % 10

            layer += 1

        return -1

        