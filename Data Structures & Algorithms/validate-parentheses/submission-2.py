class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pPair = {")":"(","]":"[","}":"{"}

        for c in s:
            if c in pPair:
                if stack and stack[-1] == pPair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) 
        return True if not stack else False