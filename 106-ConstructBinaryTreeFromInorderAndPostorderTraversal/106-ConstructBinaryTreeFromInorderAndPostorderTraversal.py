# Last updated: 6/11/2025, 10:34:59 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder:
            return None

        root = TreeNode(postorder[-1])
        rootIndex = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:rootIndex], postorder[0:rootIndex])
        root.right= self.buildTree(inorder[rootIndex+1:], postorder[rootIndex:-1])

        return root


