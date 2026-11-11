class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def traverse(p1, p2, p3):
            if p3 == len(s3):
                if p1 == len(s1) and p2 == len(s2):
                    return True
                return False
            
            c = s3[p3]
            pick1 = pick2 = False
            if p1 < len(s1) and s1[p1] == c:
                pick1 = traverse(p1+1, p2, p3+1)
            if p2 < len(s2) and s2[p2] == c:
                pick2 = traverse(p1, p2+1, p3+1)
            return pick1 or pick2

        return traverse(0,0,0)
            

            