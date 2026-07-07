class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        magic_box = set()

        for candy in nums:
            if candy in magic_box:
                return True
            magic_box.add(candy)

        return False