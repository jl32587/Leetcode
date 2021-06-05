# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        q = [root]
        mindepth = 0
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right) 
                if not node.left and not node.right:
                    return mindepth + 1
            mindepth += 1
        return mindepth