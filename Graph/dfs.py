visited = set()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def isInBound(r, c):
    return 0 <= r <= len(grid) - 1 and 0 <= c <= len(grid[0]) - 1


def dfs(r, c):

    if (r, c) in visited:
        return

    visited.add((r, c))

    for dir in directions:
        new_x = r + dir[0]
        new_y = c + dir[1]
        if ('''the condition to test if the next neighbor is visitable'''):
            dfs(new_x, new_y)


for r in range(len(grid)):
    for c in range(len(grid[0])):
        dfs(r, c)
