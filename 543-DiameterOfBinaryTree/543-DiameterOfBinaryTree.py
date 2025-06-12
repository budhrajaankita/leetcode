# Last updated: 6/11/2025, 10:34:30 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def findDiameter(node, res):
            if not node:
                return 0
            left = findDiameter(node.left, res) if node.left else 0
            right = findDiameter(node.right, res) if node.right else 0

            res[0] = max(res[0], left + right)

            return 1 + max(left, right)

        res = [0]

        findDiameter(root, res)

        return res[0]

