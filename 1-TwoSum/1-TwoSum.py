// Last updated: 3/21/2025, 10:58:41 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, v in enumerate(nums):
            a = target - nums[i]
            if a in d:
                return [i, d[a]]

            d[v] = i

        return []