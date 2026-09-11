class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s)-1
        while left < right :
            while left < right and not self.helper(s[left]):
                left+=1
            while right > left and not self.helper(s[right]):
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True
    
    #helper function to only take alphanumerical characters by making sure the number of the character is in the ASCII number range
    def helper(self,c):
        return ((ord('A') <= ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) <= ord('z')) or
                (ord('0') <= ord(c) <= ord('9')))