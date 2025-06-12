# Last updated: 6/11/2025, 10:34:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:


        def convert(l):
            if not l:
                return None
        
            root = (len(l) -1 )// 2
            rootNode = TreeNode(l[root])
            rootNode.left = convert(l[0:root])
            rootNode.right = convert(l[root+1:])

            return rootNode

        return convert(nums)

        