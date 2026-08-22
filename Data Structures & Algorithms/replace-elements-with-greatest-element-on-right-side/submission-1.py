class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [0] * len(arr)
        currentMax = -1
        
        # Loop from RIGHT to LEFT (len of array -1 down to 0)
        for i in range(len(arr) - 1, -1, -1):
            result[i] = currentMax
            currentMax = max(currentMax, arr[i])
            
        return result