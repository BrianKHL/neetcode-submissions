class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        newCount = 0

        for i in nums:
            if i == 1:
                count += 1
                if (newCount < count):
                    newCount = count
                # newCount = max(newCount, count)
            else:
                count = 0
                
        return newCount
