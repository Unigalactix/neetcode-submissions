class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0,len(height)-1
        maxLeft, maxRight = height[left],height[right]
        res=0

        while left<right:
            if maxLeft < maxRight:
                left+=1
                maxLeft=max(maxLeft,height[left])
                res+=maxLeft-height[left]
            else:
                right-=1
                maxRight=max(maxRight,height[right])
                res+=maxRight-height[right]
        return res

"""The webpage shows a puzzle called [Trapping Rain Water](https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150).

### What the Puzzle Is About

Imagine you built towers out of toy blocks in a row. Some towers are tall, and some are short.

When it rains from the sky, water falls between the towers. The water gets trapped in the low spots and makes little puddles, just like a bathtub!

The goal is to count how many blocks of water get stuck in the puddles before the water spills out the sides.

### How to Find the Answer

1. Water can only stay in a puddle if there is a wall on the left and a wall on the right to hold it in.
2. The water can only fill up as high as the shorter wall. If it goes higher, it spills out!
3. To find how deep a puddle is on any block, look at the tallest wall to the left and the tallest wall to the right. Take the shorter wall, and take away the height of the floor underneath.

### The Question and Answer

* **The Question:** If the block heights are `[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]`, how much water stays trapped?
* **The Answer:** Exactly **9** blocks of water get trapped in the puddles!"""