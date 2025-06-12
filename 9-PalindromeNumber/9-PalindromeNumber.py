# Last updated: 6/11/2025, 10:35:14 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)[::-1]
        if str(x) == rev :
            return True
        else:
            return False