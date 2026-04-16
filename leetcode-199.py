# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque()
        if root:
            queue.append(root)
        rightview = []
        while queue:
            nex = deque()
            rightview.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            queue = nex
        
        return rightview