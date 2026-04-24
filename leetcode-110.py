# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.out =True

        def dfs(node, depth):
            if node is None:
                return depth
            lef = depth
            righ = depth
            if node.left:
                lef = dfs(node.left, depth+1)
            if node.right:
                righ = dfs(node.right, depth+1)
            if abs(lef-righ)>1:
                self.out =False
            return(max(lef,righ))
            
        dfs(root,0)  
        return self.out