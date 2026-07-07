class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output=[1]*n
        left_mul=1
        for i in range(n):
            output[i]=left_mul
            left_mul*=nums[i]
        right_mul=1
        for i in range(n-1,-1,-1):
            output[i]*=right_mul
            right_mul*=nums[i]
        return output