# Last updated: 6/11/2025, 10:35:16 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        def isPal(l, r):
            while l > 0 and r < len(s)-1 and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            return l, r, r-l+1

        left = right = maxLen = 0
        
        for i in range(len(s)-1):
            l1, r1, len1 = isPal(i, i)
            if len1 > maxLen:
                maxLen = len1
                left = l1
                right = r1
            
            if s[i] == s[i+1]:
                l2, r2, len2 = isPal(i, i+1)
                if len2 > maxLen:
                    maxLen = len2
                    left = l2
                    right = r2

        return s[left:right + 1]

