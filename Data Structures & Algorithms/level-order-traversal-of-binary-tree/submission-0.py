# video solution (same as solution 2 -- BFS)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = [] 
            for i in range(qLen):
                node = q.popleft() # first in, first out先进先出
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: 
                res.append(level) # make sure the level is not empty (edge case)

        return res
