# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.out = 0
        def dfs(node):
            
            if node.right is None and node.left is None:
                print(node.val)
                return 1
            else:
                if node.left:
                    leftH = dfs(node.left)
                else:
                    leftH = 0

                if node.right:
                    rightH = dfs(node.right)
                else:
                    rightH = 0

                self.out = max(leftH+rightH,self.out)
                print(node.val)
                return 1+max(leftH,rightH)
        dfs(root)

        return self.out