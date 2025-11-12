def numIslands(self, grid: List[List[str]]) -> int:        
        # if a cell is 1, begin DFS on that cell. Mark a cell as visited by changing it to 1
        rows = len(grid)
        cols = len(grid[0])

        def DFS(row, col):
            # process current cell by mark as visited 
            grid[row][col] = '0'

            # check all neighbors
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc 
                if newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols and grid[newRow][newCol] == '1':
                    DFS(newRow, newCol)               

        cnt = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    cnt += 1
                    DFS(row, col)

        return cnt 