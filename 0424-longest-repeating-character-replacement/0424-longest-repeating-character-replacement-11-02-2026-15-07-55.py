class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            counts[s[r]] += 1  
            while (total := r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, total)
        return res

        

            

            


            