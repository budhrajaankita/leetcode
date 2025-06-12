# Last updated: 6/11/2025, 10:34:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def search(root, result):
            if not root:
                return
                
            search(root.left, result)
            search(root.right, result)
            result.append(root.val)
        
        result = []
        search(root, result)
        return result

        
