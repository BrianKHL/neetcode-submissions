class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #No need to store hash map (key-value), only value needed
        checked = set()

        for i in nums:
            if i in checked:
                return True

            checked.add(i)

        return False
