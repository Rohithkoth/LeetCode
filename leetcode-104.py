# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxdepth = 0
        
        
        def dfs(node,depth):
            if node:
                depth +=1
                self.maxdepth = max(self.maxdepth,depth)
                dfs(node.left,depth)
                dfs(node.right,depth)
            
            return


        dfs(root, 0)
        return self.maxdepth
            