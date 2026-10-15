class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = [-1] * len(arr)

        for i in range(len(arr) - 1):
            new_arr[i] = max(arr[i+1:])

        return new_arr
