# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.total=float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            current=node.val+left+right

            self.total=max(current,self.total)

            return node.val+max(left,right)
        dfs(root)

        return self.total
            
