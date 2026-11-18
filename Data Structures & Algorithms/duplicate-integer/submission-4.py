class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = set()

        for i in nums:
            if i in checked:
                return True
                
            #Need to careful on indentation    
            checked.add(i)

        return False