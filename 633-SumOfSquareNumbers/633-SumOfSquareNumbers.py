# Last updated: 6/11/2025, 10:34:26 PM
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        a = 0
        b = int(math.sqrt(c)) + 1

        while a <= b:
            summ = a**2 + b**2
            if summ == c:
                return True
            elif summ < c:
                a+=1
            else:
                b -=1

        return False
            
        