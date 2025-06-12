# Last updated: 6/11/2025, 10:34:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:

        if not a and not b:
            return True
        if not a or not b:
            return False

        return (a.val == b.val and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right))


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root or not subRoot:
            return False

        q = [root]

        while q:
            node = q.pop()
            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False
                

            


        