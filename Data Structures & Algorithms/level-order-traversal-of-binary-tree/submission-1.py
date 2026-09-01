from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            curr = []
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # 1. Process the CURRENT node
                curr.append(node.val)
                
                # 2. Queue children for the NEXT level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(curr)
            
        return res