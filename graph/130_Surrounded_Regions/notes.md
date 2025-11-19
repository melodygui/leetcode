### Summary
- This problem is great to learn the concept of multi-source BFS/DFS, since we are running DFS from every 'O' node on the border, which together represents a single region / type of state, which is "connected to the boundary" in this problem. 
- This is in contrast to `LC 200: Number of Islands`, where each DFS is independent and corresponds to exactly one island. We simply run it multiple times to find all islands. 

### General Template for Multi-Source DFS
```python
# Given: grid or graph

# 1. Identify all starting nodes (sources)
sources = []
for each node:
    if node meets source criteria:
        sources.append(node)

# 2. Run DFS from each source (one DFS function, multiple roots)
def dfs(node):
    mark node as visited
    for each neighbor:
        if not visited and neighbor is valid:
            dfs(neighbor)

# 3. Launch DFS from every source
for s in sources:
    if not visited[s]:
        dfs(s)

```

### Complexity
- **Time**: `O(number of cells in the grid) = O(rows * col)` (linear in the size of the problem). Each cell is visited at most a constant number of times (once in DFS, once in the final sweep).
- **Space**: `O(number of cells in the grid)` worst-case recursion stack if the entire board is one big connected 'O' region.

