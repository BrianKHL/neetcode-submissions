class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # rightMost = -1
        newArr = []

        for i in range(len(arr)):
            if(i != len(arr) - 1):
                newArr.append(max(arr[i+1:]))
            else:
                newArr.append(-1)
        return newArr