# Last updated: 6/11/2025, 10:34:35 PM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # self.psum = []

        self.psum = [0] * (len(nums)+1)

        for i in range(len(nums)):
            self.psum[i] = self.psum[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.psum[right] - self.psum[left-1]    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)