# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
            Optimal solution is O(log^2 n) using two binary search to find how many nodes in last level
            First do an outer binary search: for each index we check during the outer binary search, 
            we use the inner binary search to check if there is a node at that index, 
            and together this is how we check what the rightmost node is
        """        
        def exists(idx):
                left = 0
                right = 2 ** (levels - 1) - 1 # there're 2^(h-1) nodes in level h, but node index is from 0 to 2^(h-1) - 1
                node = root

                # walk down the tree - at each level, decide if go left or right, until reach last level
                for level in range(levels - 1): 
                    mid = (left + right) // 2
                    if idx <= mid:
                        # target idx is in left half
                        node = node.left 
                        right = mid 
                    else:
                        # target idx is in right half 
                        node = node.right
                        left = mid + 1

                    if node is None:
                        return False                

                return True      

        # empty tree
        if not root:
            return 0

        # first find how many levels are in the tree (go as far left as possible)
        levels = 0 
        node = root
        while node:
            levels += 1
            node = node.left
        
        # count all nodes except the last level : 2 ^ (levels - 1) - 1
        nodes = 2 ** (levels - 1) - 1

        # check how many nodes are in the last level - binary search to find the FIRST MISSING NODE
        left = 0
        right = 2 ** (levels - 1) # number of possible nodes on last level

        while left < right:
            mid = (left + right) // 2
            # check if mid index exists by walking down the tree from root, using binary search to decide if a node is in left or right half

            if exists(mid):
                # if node at mid exists, first missing must be to right of mid 
                left = mid + 1
            else: 
                # if node at mid does not exist, first missing is at mid or to the left
                right = mid 
        
        # when we come out of the while loop, left == high == # nodes in last level 
        return nodes + right