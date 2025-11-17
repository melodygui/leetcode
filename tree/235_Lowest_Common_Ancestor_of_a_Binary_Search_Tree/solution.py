# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        traverse the tree and return the first node where the path to p and q diverge
        """
        if not root:
            return None

        node = root 
        # While p and q are both on the same side of node, move down
        while (node.val - p.val) * (node.val - q.val) > 0: # (node - p) and (node - q) have the same sign: they're both smaller or greater than node
            if p.val > node.val:
                node = node.right 
            else:
                # p.val < node.val (can't be equal or the condition in while loop would be 0)
                node = node.left

        return node 