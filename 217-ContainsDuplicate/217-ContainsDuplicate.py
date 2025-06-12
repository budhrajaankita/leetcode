# Last updated: 6/11/2025, 10:34:42 PM
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # a = Counter(nums)
        # for k,v in a.items():
        #     if v > 1:
        #         return True
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


        