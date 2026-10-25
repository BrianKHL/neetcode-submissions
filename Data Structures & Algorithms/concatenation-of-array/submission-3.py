class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            ans.append(i)
        ans *= 2
        return ans