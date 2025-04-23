class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        formatted = ''.join(char for char in s.lower() if char.isalnum())

        left = 0
        right = len(formatted) - 1
        # print(formatted)
        while left <= right:
            if formatted[left] != formatted[right]:
                return False
            
            left += 1
            right -= 1
        
        return True

mystr = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(mystr))