class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # problem interpretation: flip a 'O' only if its entire island does not touch the border
        """
        goal: flip a 'O' only if its entire island does not touch the border
        key idea: start from 'O' nodes on the border and mark all 'O' nodes reachable from the border as 'E'         
        """
        rows = len(board)
        cols = len(board[0])

        def DFS(row, col):  
            board[row][col] = 'E' 

            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc 
                # check if rows or cols are out of bounds 
                if newRow < 0 or newCol < 0 or newRow >= rows or newCol >= cols:
                    continue
                
                if board[newRow][newCol] == 'O':
                    DFS(newRow, newCol)

        # STEP 1: start from 'O' nodes on the border and mark all 'O' nodes reachable from the border as 'E'
        # check all cells in first and last row 
        for col in range(cols):
            if board[0][col] == 'O':
                DFS(0, col) # mark all nodes on / reachable from the border as 'E' for escaped from flipping
            if board[rows - 1][col] == 'O':
                DFS(rows - 1, col)

        # check all rows (except first and last) in first and last col
        for row in range(1, rows - 1): # from second row to second to last row 
            if board[row][0] == 'O':
                DFS(row, 0)
            if board[row][cols - 1] == 'O':
                DFS(row, cols - 1)
        
        # STEP 2: all remaining 'O's on the graph must be not reachable from border, so mark them as 'X'
        # also change all 'E' nodes back to 'O
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'E':
                    board[row][col] = 'O'
        
        return 