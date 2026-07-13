class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_car_spot = 0 

        for toy in nums:
            if toy != val:
                nums[next_car_spot] = toy
                next_car_spot += 1

        return next_car_spot