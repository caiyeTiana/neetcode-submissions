# solution 1 -- DFS (same as video) 超时了 ！但还是学习这个吧，还是同步到github里了

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) # in Python, mid + 1不在其中，所以这里就是只到mid; 
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


        