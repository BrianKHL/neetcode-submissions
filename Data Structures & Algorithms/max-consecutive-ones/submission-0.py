class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

#First, counter start if its 1 and stop counting if meets 0
#Second, when it hits length then stop and check which one has the highest accmulation
#Third, do it until hit the length and compare with previous counter and new counter. 
#If the new counter is bigger keep the biggest ones.
# Need two variables currentCounter and maxCounter 

        current_counter = 0 
        max_counter = 0

        for num in nums:
            if num == 1:
                current_counter += 1

                if current_counter > max_counter:
                    max_counter = current_counter
            else:
                current_counter = 0
        return max_counter