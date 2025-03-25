# Last updated: 3/25/2025, 1:10:10 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        

        q = deque()
        q.append(root)

        res = []

        while q:
            temp = []
           
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)


                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(temp)

        return res

                


        