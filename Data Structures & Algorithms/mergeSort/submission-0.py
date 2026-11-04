# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # 3 pointer needed (2 needed for sorting, the other 1 needed for mergeing for the last one at the very end)
        # split into half (full length of index / 2)
        # if the size of the array is <= 1, return array (which means base == 1)
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)


    def mergeSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs

        mid = (s + e)  // 2 # s + (e - s) // 2

        self.mergeSortHelper(pairs, s, mid)
        self.mergeSortHelper(pairs, mid+1, e)

        self.merge(pairs, s, mid, e)

        return pairs

    def merge(self, arr, s, mid, e):
        Left = arr[s:mid+1]
        Right = arr[mid+1:e+1]

        i = 0 # index for Left
        j = 0 # index for Right
        k = s # index for arr

        #Merge the two sorted halfs
        while i < len(Left) and j < len(Right):
            if Left[i].key <= Right[j].key:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
        
        #One of the halfs will have elements remaining
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1


