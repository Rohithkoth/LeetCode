# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        # if root:
        #     self.count =1

        def dfs(node,currmax):
            newmax = currmax
            print(node.val,currmax)
            if node.val >= currmax:
                self.count+=1
                newmax =node.val
            if node.left:
                dfs(node.left, newmax)
            if node.right:
                dfs(node.right,newmax)

            return
        
        dfs(root,root.val)
        return self.count
        