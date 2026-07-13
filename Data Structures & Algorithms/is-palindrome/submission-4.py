class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        right = lens = len(s) - 1 
        left = 0

        while right > left:
            while s[left].isalnum() == False:
                if left == len(s) - 1:
                    return True
                left += 1
            while s[right].isalnum() == False:
                if right == 0:
                    return True
                right -= 1
            
            if s[right] != s[left]:
                return False
            
            right -= 1
            left += 1

        return True