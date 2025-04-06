# Last updated: 4/5/2025, 10:07:15 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        maxPal = ""

        #odd
        for i in range(1,len(s)):
            l = r = i
            while l-1 >=0 and r+1 <= len(s)-1 and s[l-1] == s[r+1]:
                l-=1
                r+=1
                # print(s[l:r+1])
            if s[l] == s[r] and (r - l + 1) > len(maxPal):
                maxPal = s[l:r+1]
        #even
            l=i-1
            r=i
            while s[l] == s[r] and l-1 >=0 and r+1 <= len(s)-1 and s[l-1] == s[r+1]:
                l-=1
                r+=1
                # print(s[l:r+1])
            if (r - l + 1) > len(maxPal) and s[l] == s[r]:
                maxPal = s[l:r+1]

        return maxPal


            
            
            

            
                







        