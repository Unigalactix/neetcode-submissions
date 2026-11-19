class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # Stores tuples of (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # Pop bars taller than current height; they can't extend past index i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                width = i - idx
                max_area = max(max_area, height * width)
                start = idx  # Current bar can extend left to where the taller bar started
            stack.append((start, h))

        # Remaining bars can extend all the way to the end of the histogram
        n = len(heights)
        for idx, height in stack:
            width = n - idx
            max_area = max(max_area, height * width)

        return max_area