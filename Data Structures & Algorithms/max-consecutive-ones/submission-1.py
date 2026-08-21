class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        curr_counter, max_counter = 0, 0

        for num in nums:
            if num == 1:
                curr_counter += 1

                if curr_counter >= max_counter:
                    max_counter = curr_counter
                
            else:
                curr_counter = 0
        return max_counter