# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lb, rb):
            if not node:
                return True
            
            if not(lb<node.val<rb):
                return False
            
            return dfs(node.left, lb, node.val) and dfs(node.right, node.val, rb)
       
        
        return dfs(root, float('-inf'), float('inf'))