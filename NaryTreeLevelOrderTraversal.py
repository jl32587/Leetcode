"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        
        if not root: return None
        
        q = [root]
        out = [[root.val]]
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node and node.children:
                    for child in node.children:
                        q.append(child)
                        level.append(child.val)
            
            if level: out.append(level)
                        
        return out