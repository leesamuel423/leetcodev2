class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    self.dfs(r, c, grid, visited)
        return count
    
    def dfs(self, r, c, grid, visited):
        r_bound = 0 <= r < len(grid)
        c_bound = 0 <= c < len(grid[0])

        if not r_bound or not c_bound or (r, c) in visited or grid[r][c] == "0":
            return
        
        visited.add((r, c))

        self.dfs(r + 1, c, grid, visited)
        self.dfs(r - 1, c, grid, visited)
        self.dfs(r, c + 1, grid, visited)
        self.dfs(r, c - 1, grid, visited)
        


"""
count = 0
set to keep track of visited locations
for each item in grid (double for loop):
    check that is 1 and not in visited set:
        count += 1
        run dfs
return count


dfs to figure out islands(row, column, grid, visited set)
    row_boundaries
    col_boundaries

    if current location is outside row_boundaries or col_boundaries or is not 1:
        return
    
    add to visited set

    run dfs on left, right, up, down

"""
        