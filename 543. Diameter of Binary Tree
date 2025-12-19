# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def height(self, root):
        if not root:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        both = self.height(root.left) + self.height(root.right)
        
        return max(left, right, both)
