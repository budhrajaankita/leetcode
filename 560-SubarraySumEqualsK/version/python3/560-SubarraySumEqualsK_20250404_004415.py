# Last updated: 4/4/2025, 12:44:15 AM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        d = defaultdict(int)
        d[0] = 1
        currSum = 0
        count = 0

        for i in range(len(nums)):
            currSum += nums[i]
            target = currSum - k
            count += d[target]

            d[currSum] += 1 


        return count




        # 7, -1, 1, 10

        # target = 7

        # runningSum = 7

        # {0:[-1], 7:[0,2], 6:[1],  }

        # result (-1:0)





        prefix = -1,0,2, 7, 17, 24

        {-1:1, 0:2, 2:1, 17:1}

        counter = 3


        