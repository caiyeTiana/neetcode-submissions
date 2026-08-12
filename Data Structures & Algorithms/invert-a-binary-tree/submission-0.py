# NeetCode solution 2 -- Depth First Search (similar to vedio)
# a, b = b, a 是 Python 的元组交换：右边先整体求值打包成一个元组 (root.right, root.left)，此时旧值已被记下，然后才拆开赋给左边。tmp由解释器隐式做了。
# video version还显式地写出了tmp
# Depth First Search： 递归的执行顺序是「一条路走到黑」再回头。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        