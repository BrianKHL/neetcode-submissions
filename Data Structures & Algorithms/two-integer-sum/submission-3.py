class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            weNeed = target - nums[i]

            if weNeed in seen:
                return [seen[weNeed], i ]

            seen[nums[i]] = i