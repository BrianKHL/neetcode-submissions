class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        
        if len(s) != len(t):
            return False

        for i,j in zip(s,t):
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            if j in count:
                count[j] -= 1
            else:
                count[j] = -1

        if all(num == 0 for num in count.values()):
            return True
        return False

            