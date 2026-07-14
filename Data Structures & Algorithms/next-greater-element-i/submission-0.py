class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # This cheat sheet will store: {number: its_next_greater_number}
        cheat_sheet = {}
        stack = []
        
        # Step 1: Look through the big line (nums2) to find matches
        for num in nums2:
            # While we have kids in our stack, and the current kid is TALLER
            # than the kid at the top of the stack...
            while stack and num > stack[-1]:
                # We found a Taller Friend! Save it in our cheat sheet
                smaller_num = stack.pop()
                cheat_sheet[smaller_num] = num
                
            # Put the current kid onto the stack to wait for their Taller Friend
            stack.append(num)
            
        # Step 2: Build our final answer list for our buddies (nums1)
        ans = []
        for num in nums1:
            # Look up our buddy in the cheat sheet. If they don't have a 
            # Taller Friend, write down -1.
            ans.append(cheat_sheet.get(num, -1))
            
        return ans        