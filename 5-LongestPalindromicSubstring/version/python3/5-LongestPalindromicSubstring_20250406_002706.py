# Last updated: 4/6/2025, 12:27:06 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        maxPal = ""

        def isPal(l, r):
            while l > 0 and r < len(s)-1 and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            return l, r, r-l+1


        #odd
        left = right = maxLen = 0
        for i in range(len(s)-1):
            l1, r1, maxlen1 = isPal(i,i)
            if maxlen1 > maxLen:
                maxLen= maxlen1
                left=l1
                right=r1

            if s[i] == s[i+1]:
                l2, r2, maxlen2 = isPal(i, i+1)
                if maxlen2 > maxLen:
                    maxLen= maxlen2
                    left=l2
                    right=r2

        return s[left:right+1]


            
            
            

            
                







        