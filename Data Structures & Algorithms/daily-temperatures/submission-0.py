class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = []  # Stores indices of days waiting for a warmer day

        for current_day, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = current_day - prev_day
            stack.append(current_day)

        return result