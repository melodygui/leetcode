### Time and Space Complexity

Time Complexity: 
- Worst case the entire grid is land so DFS will run deep, exploring every cell, taking O(m x n) time.

Space Complexity: 
- Since in the worst case, the recursive call stack will be m x n levels deep. It takes up O(m x n) space. 