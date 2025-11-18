# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Each DFS(node) calculates the max path sum of the subtree rooted at node and updates the answer  
        Each DFS(node) returns the max path length of that subtree
        """      
        ans = float("-inf")

        def DFS(node):  
            nonlocal ans

            # base case: leaf node, path length is 0
            if not node:
                return 0 
            
            # to decide whether or not to include left or right branch or both, we only include them if they're positive and add to the sum            
            leftGain = max(DFS(node.left), 0)
            rightGain = max(DFS(node.right), 0)

            currSum = leftGain + rightGain + node.val           
            ans = max(ans, currSum) 

            # max path length is max of left path length and right path length, combined with the curr node val
            return max(leftGain, rightGain) + node.val
            
        DFS(root)
        return ans