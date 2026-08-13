# solution 2 -- DFS (same as video)

# 每个节点要检查的不是父亲，而是从根一路传下来的开区间 (left, right)。node.val 必须严格落在 (left, right) 里

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # isValidBST 的签名被 LeetCode 定死了，只能收一个 root。但递归需要多带两个参数（当前节点允许的上下界），所以自己造一个能收三个参数的valid。写在里边是为了不污染外部命名空间。
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))




