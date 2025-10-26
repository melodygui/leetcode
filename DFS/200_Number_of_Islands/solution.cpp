#include <vector>
using namespace std;

/*
Difficulty: medium
Description:
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
*/
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        
        // go through all cells in grid and run DFS on every unvisited land to find all connected land cells 
        for (int row = 0; row < grid.size(); row++) {
            for (int col = 0; col < grid[0].size(); col++) {
                if (grid[row][col] == '1') {
                    count++;
                    DFS(grid, row, col);
                }
            }
        }
        
        return count;
    }
    
private:
    /*
        DFS finds all connected land cells and mark them as visited 
    */
    void DFS(vector<vector<char>>& grid, int row, int col) {
        // Base case: out of bounds or water or already visited
        if (row < 0 || row >= grid.size() || 
            col < 0 || col >= grid[0].size() || 
            grid[row][col] != '1') {
            return;
        }
        
        // Mark as visited 
        grid[row][col] = '0';
        
        // Explore all 4 directions
        DFS(grid, row + 1, col);  // down
        DFS(grid, row - 1, col);  // up
        DFS(grid, row, col + 1);  // right
        DFS(grid, row, col - 1);  // left
    }
};