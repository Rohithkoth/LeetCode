# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node:
                print(node.val)
            if node is None and subRoot is not None:
                return False
            else:
                return dfs(node.left) or dfs(node.right)  or match(node,subRoot)

        def match(node,sub):
            if node is None and sub is None:
                return True
            elif node is None or sub is None or node.val != sub.val:
                return False
            else:
                return match(node.left,sub.left) and match(node.right, sub.right)
            
        return dfs(root)
 