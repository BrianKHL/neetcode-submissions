class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Pointer
        k = 0

        for i in range(len(nums)):
            if nums[i]!= val:
                #Partition
                nums[k] = nums[i]
                k += 1
        return k