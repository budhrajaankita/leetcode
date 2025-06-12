# Last updated: 6/11/2025, 10:35:02 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m-1
        j = n-1
        curr = m+n-1



        while i >=0 or j>=0:
            if i < 0:
                nums1[curr] = nums2[j]
                j-=1
            elif j < 0:
                nums1[curr] = nums1[i]
                i-=1

            elif nums1[i] > nums2[j]:
                nums1[curr] = nums1[i]
                i -= 1
            else:
                nums1[curr] = nums2[j]
                j-=1
            curr -= 1


        