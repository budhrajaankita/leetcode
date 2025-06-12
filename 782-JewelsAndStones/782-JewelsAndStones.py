# Last updated: 6/11/2025, 10:34:24 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels= set(jewels)
        for s in stones:
            if s in jewels:
                count += 1

        return count