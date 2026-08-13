# similar to solution 4 - Iterative DFS (Optimal)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack: # in video, here is "and" -> debug by claude
            while cur: 
                stack.append(cur)
                cur = cur.left # go to left as much as we can

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right 



        