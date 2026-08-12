# NeetCode solution 1 - ecursive DFS
#只看了video的前两个解法，第三个Iterative DFS (Stack)没看：1.recursive DFS; 2. BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))