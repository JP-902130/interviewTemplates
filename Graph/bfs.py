from collections import deque
rooms = [[]]  # The matrix

INF = 2147483647
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = set()
queue = deque()
level = 0


def isInBound(r, c):
    return 0 <= r <= len(rooms) - 1 and 0 <= c <= len(rooms[0]) - 1


def condition():
    pass


# Add all starting coordinates
for r in range(len(rooms)):
    for c in range(len(rooms[0])):
        if rooms[r][c] == 0:
            queue.append((r, c))
            visited.add((r, c))

while queue:
    for i in range(len(queue)):
        r, c = queue.popleft()
        rooms[r][c] = level
        for dir in directions:
            nextR = dir[0] + r
            nextC = dir[1] + c
            if isInBound(nextR, nextC) and (nextR, nextC) not in visited and condition():
                queue.append((nextR, nextC))
                visited.add((nextR, nextC))
    level += 1
