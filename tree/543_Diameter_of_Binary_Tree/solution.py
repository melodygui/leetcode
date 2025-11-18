# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        during each recursion, for the node, calculate the left branch length, and right branch length 
        each DFS(node) CALCULATES the length of longest path that passes through this node
        each DFS(node) RETURNS the height of the subtree rooted at this node (aka. the number of edges from the current node to its deepest descendant)
        """
        if not root:
            return 0 

        longest = 0        

        def DFS(node):
            nonlocal longest 

            # base case: leaf node 
            if not node.left and not node.right:
                return 0 

            leftBranch, rightBranch = 0, 0
            if node.left:
                leftBranch = 1 + DFS(node.left)
            if node.right:
                rightBranch = 1 + DFS(node.right)

            currLength = leftBranch + rightBranch # the length of the longest path at this node (imagine going through the node, if both branches are not empty)
            longest = max(longest, currLength)
        
            return max(leftBranch, rightBranch)
        
        DFS(root)

        return longest