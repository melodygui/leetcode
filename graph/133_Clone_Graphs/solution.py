"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # each recursion should clone that node and add all its neighbors (cloned)
     
        # create a dict to store mapping from old(original) node to cloned node 
        oldToCloned = {}

        def DFS(node):
            # clone current node
            cloned = Node(node.val)
            # add this node and its cloned to the hash map 
            oldToCloned[node] = cloned

            # add all its neighbors (every neighbor must be cloned as well)
            for neighbor in node.neighbors:
                if neighbor in oldToCloned:
                    clonedNeighbor = oldToCloned[neighbor]
                else:
                    clonedNeighbor = DFS(neighbor)
                cloned.neighbors.append(clonedNeighbor)
            
            return cloned 
        
        return DFS(node)
