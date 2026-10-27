class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s1): return False

        s1_counts = Counter(s1)
        s2_counts = Counter(s2[:len(s1)])
        if s1_counts == s2_counts: return True
        for i in range(len(s1), len(s2)):
            s2_counts[s2[i-len(s1)]] -= 1
            if s2_counts[s2[i-len(s1)]] == 0: del s2_counts[s2[i-len(s1)]]
            s2_counts[s2[i]] += 1
            if s1_counts == s2_counts: return True
        return False
        