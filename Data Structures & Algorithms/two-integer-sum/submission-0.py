class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        notepad={}
        for current_chair, num in enumerate(nums):
            needed_number = target - num
            if needed_number in notepad:
                return[notepad[needed_number],current_chair]
            notepad[num]=current_chair