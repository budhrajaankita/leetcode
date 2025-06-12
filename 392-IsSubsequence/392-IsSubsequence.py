# Last updated: 6/11/2025, 10:34:32 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:        
        l = 0
        r = 0
        if s == "":
            return True
        
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l+=1
            r+=1

        return l == len(s)

                