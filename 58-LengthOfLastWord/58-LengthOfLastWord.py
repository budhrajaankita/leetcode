# Last updated: 6/11/2025, 10:35:06 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spl = s.split(" ")

        for i in range(len(spl) - 1, -1, -1):
            if spl[i].isalnum():
                return len(spl[i])



        