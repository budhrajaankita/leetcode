# Last updated: 4/6/2025, 9:42:10 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # visited = {}
        # def dfs(root):
        #     if not root:
        #         return None
        #     if root.val in visited:
        #         return visited[root.val]
        #     newNode = Node(root.val, [])
        #     visited[root.val] = newNode
        #     for neighbor in root.neighbors:
        #         newNode.neighbors.append(dfs(neighbor))
        #     return newNode
        # return dfs(node)
        # # if node is None:
        #     return None
        # print(node.val)
        # print(node.neighbors)
        # visited = set()
        # d = {}


        visited = {}
        def dfs(node):
            if not node:
                return None
            
            if node.val in visited:
                return visited[node.val]
            
            new = Node(node.val)
            visited[node.val] = new

            for nei in node.neighbors:
                new.neighbors.append(dfs(nei))
            return new
        
        # root = Node(1)
        

        return dfs(node)
            

        


        