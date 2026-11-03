class Solution:
    def helper(self, candidates, target):
        res = []
        seen = set()
        for i, n in enumerate(candidates):
            if n in seen: continue
            if target - n == 0:
                res.append([n])
            elif target - n > 0:
                sub = self.combinationSum2(candidates[i+1:], target - n)
                res.extend([[n] + l for l in sub])
            seen.add(n)
        return res

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        return self.helper(sorted(candidates), target)