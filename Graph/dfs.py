class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def isInBound(r, c):
            return 0 <= r <= len(grid) - 1 and 0 <= c <= len(grid[0]) - 1

        def dfs(r, c):

            # Boundary check
            if isInBound(r, c) == False:
                return
            # Visited check
            if (r, c) in visited:
                return
            # Some other condition
            if grid[r][c] == '0':
                return
            visited.add((r, c))

            for dir in directions:
                newR = dir[0] + r
                newC = dir[1] + c
                dfs(newR, newC)

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # Things that might be modified here
                if (r, c) not in visited and grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count
