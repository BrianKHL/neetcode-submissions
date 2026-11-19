class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checked = {}

        if len(s) != len(t):
            return False

        for i,j in zip(s,t):
            if i in checked:
                checked[i] += 1
            else:
                checked[i] = 1

            if j in checked:
                checked[j] -= 1
            else:
                checked[j] = -1

        if all(num == 0 for num in checked.values()):
            return True
        return False