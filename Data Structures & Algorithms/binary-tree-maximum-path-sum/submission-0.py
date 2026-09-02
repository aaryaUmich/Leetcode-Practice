# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def postOrder(node):
            nonlocal res
            if not node:
                return 0
            
            # 1. Compute max contribution from left and right subtrees (clamp negative values to 0)
            left = max(postOrder(node.left), 0)
            right = max(postOrder(node.right), 0)

            # 2. Update global max path sum that splits at current node
            res = max(res, node.val + left + right)

            # 3. Return max single path continuing upward to parent
            return node.val + max(left, right)

        postOrder(root)
        return res