# Last updated: 6/11/2025, 10:34:46 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = deque()
        q.append(root)

        if not root:
            return []
        
        res = []
        while q:
           levelSize= len(q)
           for i in range(levelSize):
                node = q.popleft()
                if i == levelSize - 1:
                    res.append(node.val)
                # if node.right:
                #     q.append(node.right)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res