class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {   
            '(': ')', 
            '[': ']',
            '{': '}'
        }

        for c in s:
            if c in pairs.keys():
                stack.append(c)
            elif c in pairs.values():
                if stack and c == pairs[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack
            