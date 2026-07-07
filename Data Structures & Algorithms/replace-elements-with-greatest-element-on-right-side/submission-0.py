class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1

        for i in range(len(arr)-1,-1,-1):
            original_val = arr[i]
            arr[i]=current_max
            current_max=max(current_max,original_val)
        return arr