class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left<right:
            width=right - left
            current_height=min(heights[left],heights[right])
            current_water=width*current_height

            max_water=max(max_water,current_water)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_water


"""Imagine you have a bunch of toy walls standing up straight, like fences of different heights. You want to pick any two walls to build a swimming pool between them so it can hold the most water!

How do you find the biggest pool?
Put one toy hand at the very first wall and your other toy hand at the very last wall. Measure how much water fits between them. Since water spills over the shortest wall, your pool's height is only as tall as the shorter fence.

To find a bigger pool, take the hand that is holding the shorter fence and move it one step closer to the middle. You keep doing this, sliding your hands inward, until they meet in the middle. The biggest puddle you find along the way is your winner!"""