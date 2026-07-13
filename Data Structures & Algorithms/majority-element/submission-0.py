class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        champion = None
        shield_points = 0

        for num in nums:
            if shield_points == 0:
                champion = num

            if num == champion:
                shield_points += 1
            else:
                shield_points -= 1
        return champion