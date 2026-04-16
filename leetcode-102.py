# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            row = []
            nex = deque()
            for i in range(len(queue)):
                ins = queue.popleft()
                row.append(ins.val)
                if ins.left:
                    nex.append(ins.left)
                if ins.right:
                    nex.append(ins.right)
            out.append(row)
            queue = nex
        return out