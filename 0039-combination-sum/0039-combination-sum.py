class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        for i, n in enumerate(candidates):
            times = 1
            while target - n * times >= 0:
                if target - n * times == 0:
                    res.append([n] * times)
                else:
                    sub_combinations = self.combinationSum(candidates[i+1:], target - n * times)
                    res.extend([l + ([n] * times) for l in sub_combinations])
                times += 1
        return res