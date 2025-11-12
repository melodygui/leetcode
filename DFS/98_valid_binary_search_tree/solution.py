# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(node, low, high):
        # step 1: base case: reached past a leaf node - an empty subtree is trivially a valid BST
        if not node:
            return True

        # step 2: pruning 
        # early return (stop recursion) if current node is not valid
        if not (low < node.val < high):
            return False

        # step 3: recursion
        # left child has to be at most node's val (upper bound so updating high)
        # right child needs to be at least node's val (lower bound so updating low)
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
    return dfs(root, float("-inf"), float("inf"))