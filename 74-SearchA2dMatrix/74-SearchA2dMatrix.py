# Last updated: 6/11/2025, 10:35:05 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target > matrix[mid][0] and target < matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1

        ROW = (lo + hi) //2
        l = 0
        h = len(matrix[ROW]) - 1

        while l <= h:
            m = (l + h) // 2
            if target == matrix[ROW][m]:
                return True
            elif target < matrix[ROW][m]:
                h = m - 1
            else:
                l = m + 1

        return False
