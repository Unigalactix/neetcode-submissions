class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_finger = 0
        right_finger = len(s)-1
        while left_finger < right_finger:
             while left_finger < right_finger and not s[left_finger].isalnum():
                left_finger +=1
             while left_finger < right_finger and not s[right_finger].isalnum():
                right_finger -=1
             if s[left_finger].lower()!=s[right_finger].lower():
                return False
             left_finger += 1
             right_finger -= 1
        return True