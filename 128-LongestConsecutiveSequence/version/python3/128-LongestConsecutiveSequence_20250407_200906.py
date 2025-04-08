# Last updated: 4/7/2025, 8:09:06 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for n in numSet:
            if n-1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
            
                longest = max(longest, length)

        return longest


        