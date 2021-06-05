# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.treeSum = 0
        
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root:
		    self.rangeSumBST(root.left,low,high)
		    self.rangeSumBST(root.right,low,high)
		    if root.val <= high and root.val >= low:
		    	self.treeSum += root.val
        return self.treeSum