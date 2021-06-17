# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def dfs(root, maxval):
            if not root: return
            if root.val >= maxval: 
                self.result += 1
            dfs(root.left, max(maxval, root.val))
            dfs(root.right, max(maxval, root.val))
        
        dfs(root, root.val)
        return self.result    