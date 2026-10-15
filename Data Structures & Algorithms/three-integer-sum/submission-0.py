class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i-1]:
                continue

            left,right = i+1, len(nums)-1
            while left < right:
                three_sum = val + nums[left]+nums[right]

                if three_sum>0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([val,nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res   


"""Imagine you have a big box of toy cards with numbers written on them. Your job is to find three cards that, when you add their numbers together, make a big fat zero.

How do you find the right cards?
First, you line up all your cards from the smallest number to the biggest number, like a neat little train. Then, you pick one card to keep still. For the other two cards, you put one finger near the front of the train and one finger near the back of the train.

You add those three numbers up. If the total is too big, you move your back finger to a smaller card. If the total is too small, you move your front finger to a bigger card. You keep sliding your fingers until you find a magic group of three that adds up to zero, and make sure you don't write down the exact same group twice!"""