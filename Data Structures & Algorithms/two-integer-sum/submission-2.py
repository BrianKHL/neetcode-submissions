class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # addition of i-th index number and j-th idex number should be same as target value

        #Rember the numbers that we have seen, so that we do not have to go over every iteration every single time
        seen = {}

        for i in range(len(nums)):
            weNeed = target - nums[i]
            

            if weNeed in seen:
                return [seen[weNeed],i]

            # Save current number
            seen[nums[i]] = i