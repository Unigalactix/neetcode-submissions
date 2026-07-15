class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_weight = sum(nums)

        left_weight = 0
        for spot, block in enumerate(nums):

            if left_weight == (total_weight - left_weight - block):
                return spot
            
            left_weight += block

        return -1