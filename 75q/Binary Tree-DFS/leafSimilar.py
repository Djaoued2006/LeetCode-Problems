from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLeaf(self,  root1 : Optional[TreeNode]) -> list[int]:
        if not root1:
            return [root1.val]
        
        if not (root1.left or root1.right):
            return [root1.val]
        
        return Solution().getLeaf(root1.left) + Solution().getLeaf(root1.right)
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = Solution().getLeaf(root1)
        leaf2 = Solution().getLeaf(root2)

        return leaf1 == leaf2
    
        