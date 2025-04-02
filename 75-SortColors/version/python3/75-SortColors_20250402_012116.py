# Last updated: 4/2/2025, 1:21:16 AM
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = Counter(nums)
        idx = 0

        for color in range(3):
            freq = count.get(color, 0)
            nums[idx : idx + freq] = [color] * freq
            idx += freq