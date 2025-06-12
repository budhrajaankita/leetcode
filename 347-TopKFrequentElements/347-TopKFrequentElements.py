# Last updated: 6/11/2025, 10:34:33 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        freq = [[] for i in range((len(nums)+1))]

        for i in nums:
            count[i] = count.get(i, 0) + 1

        
        for key,v in count.items():
            freq[v].append(key)

        res = []

        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

