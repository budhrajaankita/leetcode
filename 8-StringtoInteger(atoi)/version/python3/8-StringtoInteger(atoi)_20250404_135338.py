# Last updated: 4/4/2025, 1:53:38 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        sign = 1
        res = 0
        if not s:
            return res
            
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                sign = -1
            s = s[1:]

        for char in s:
            
            if not char.isdigit():
                break

            res = res * 10 + int(char)

        res = sign * res

        if res > 2**31 -1:
            res = 2**31 -1
        elif res < -2**31:
            res = -2**31

        return res



        return 

        