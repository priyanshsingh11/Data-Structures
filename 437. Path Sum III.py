# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        def dfs(root,curr_sum):
            if not root: return 0

            curr_sum+=root.val
            count=1 if curr_sum==targetSum else 0

            count+=dfs(root.left,curr_sum)
            count+=dfs(root.right,curr_sum)

            count+=dfs(root.left,0)
            count+=dfs(root.right,0)

            return count
        return dfs(root,0)

